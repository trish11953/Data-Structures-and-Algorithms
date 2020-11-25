############################################################
# CMPSC 442: Homework 4
############################################################

student_name = "Trisha Mandal"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import copy

############################################################
# Section 1: Propositional Logic
############################################################

class Expr(object):
    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

class Atom(Expr):
    def __init__(self, name):
        self.name = name
        self.hashable = name

    def __eq__(self, other):
        if type(self) == type(other):
            if self.name == other.name:
                return True
        return False

    def __repr__(self):
        return "Atom(" + self.name + ")"

    def atom_names(self):
        sol = {self.name}
        return sol

    def evaluate(self, assignment):
        if assignment[self.name]:
            return True
        else:
            return False

    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def to_cnf(self):
        return self


class Not(Expr):
    def __init__(self, arg):
        self.arg = arg
        self.hashable = arg

    def __eq__(self, other):
        p1 = type(self) == type(other)
        p2 = self.arg == other.arg
        return p1 and p2

    def __repr__(self):
        return "Not({})".format(self.arg)

    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def atom_names(self):
        sol = self.arg.atom_names()
        return sol

    def evaluate(self, assignment):
        sol = not self.arg.evaluate(assignment)
        return sol

    def to_cnf(self):
        if type(self.arg) == Atom:
            return self
        if type(self.arg) == Implies:
            r = self.arg.right
            l = self.arg.left
            sol = And(l, Not(r)).to_cnf()
            return sol
        if type(self.arg) == And:
            con = self.arg.conjuncts
            sol = Or(*map(Not, con)).to_cnf()
            return sol
        if type(self.arg) == Not:
            sol = self.arg.arg.to_cnf()
            return sol
        if type(self.arg) == Iff:
            r = self.arg.right
            l = self.arg.left
            sol = Or(Not(Implies(l, r)),
                     Not(Implies(r, l))).to_cnf()
            return sol
        if type(self.arg) == Or:
            o = self.arg.disjuncts
            sol = And(*map(Not, o)).to_cnf()
            return sol


class And(Expr):
    def __init__(self, *conjuncts):
        self.conjuncts = frozenset(conjuncts)
        self.hashable = self.conjuncts

    def __eq__(self, other):
        p1 = type(self) == type(other)
        p2 = self.conjuncts == other.conjuncts
        sol = p1 and p2
        return sol

    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def __repr__(self):
        l = len(self.conjuncts)
        s = ["{}, "] * l
        s = "".join(s).strip()[:-1]
        s = "And(" + s + ")"
        sol = s.format(*self.conjuncts)
        return sol

    def atom_names(self):
        n = set()
        for i in self.conjuncts:
            n = n.union(i.atom_names())
        return n

    def evaluate(self, assignment):
        for a in self.conjuncts:
            if not a.evaluate(assignment):
                return False
        return True

    def to_cnf(self):
        nf = None
        temp = map(lambda x: x.to_cnf(), self.conjuncts)
        for expression in set(temp):
            if not nf:
                nf = expression
            elif type(nf) == Atom:
                if type(expression) != And:
                    nf = And(nf, expression)
                else:
                    nf = And(nf, *expression.conjuncts)
            elif type(nf) == Not:
                if type(expression) != And:
                    nf = And(nf, expression)
                else:
                    nf = And(nf, *expression.conjuncts)
            elif type(nf) == And:
                if type(expression) != And:
                    newset = set()
                    newset.add(expression)
                    nf = And(*nf.conjuncts.union(newset))
                else:
                    nf = And(*expression.conjuncts.union(nf.conjuncts))
            else:
                if type(expression) != And:
                    nf = And(nf, expression)
                else:
                    newset2 = set()
                    newset2.add(nf)
                    newset2 = expression.conjuncts.union(newset2)
                    nf = And(*newset2)
        return nf



class Or(Expr):
    def __init__(self, *disjuncts):
        self.disjuncts = frozenset(disjuncts)
        self.hashable = self.disjuncts

    def __eq__(self, other):
        p1 = type(self) == type(other)
        p2 = self.disjuncts == other.disjuncts
        sol = p1 and p2
        return sol

    def __repr__(self):
        l = len(self.disjuncts)
        s = ["{}, "] * l
        s = "".join(s).strip()[:-1]
        s = "Or(" + s + ")"
        sol = s.format(*self.disjuncts)
        return sol

    def atom_names(self):
        n = set()
        for i in self.disjuncts:
            n.update(i.atom_names())
        return n

    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def evaluate(self, assignment):
        for i in self.disjuncts:
            if i.evaluate(assignment):
                return True
        return False

    def to_cnf(self):
        lst = []
        for value in self.disjuncts:
            if type(value) != type(self):
                lst.append(value.to_cnf())
            else:
                lst = [i.to_cnf() for i in value.disjuncts]

        nO = Or(*lst)
        for value in nO.disjuncts:
            if isinstance(value, And):
                nAlist = [i for i in nO.disjuncts if value is not i]
                oAlist = [i for i in value.conjuncts]
                retAlist = []
                for k in oAlist:
                    nOlist = [k]
                    for new in nAlist:
                        nOlist.append(new)
                    retOlist = Or(*nOlist).to_cnf()
                    retAlist.append(retOlist)
                return And(*retAlist).to_cnf()
        return Or(*lst)


class Implies(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.hashable = (left, right)

    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def __eq__(self, other):
        if self.hashable == other.hashable:
            return True
        else:
            return False

    def __repr__(self):
        r = self.right
        l = self.left
        sol = "Implies(" + repr(l) + ", " + repr(r) + ")"
        return sol

    def atom_names(self):
        p1 = self.left.atom_names()
        p2 = self.right.atom_names()
        return p1.union(p2)

    def evaluate(self, assignment):
        r = self.right.evaluate(assignment)
        l = self.left.evaluate(assignment)
        if l and not r:
            return False
        else:
            return True

    def to_cnf(self):
        r = self.right
        l = self.left
        ret = Or(Not(l), r).to_cnf()
        return ret



class Iff(Expr):
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.hashable = (left, right)

    def __eq__(self, other):
        r = self.right
        l = self.left
        otherr = other.right
        otherl = other.left
        p1 = type(self) == type(other)
        p2 = (l == otherr and r == otherl)
        p3 = (l == otherl and r == otherr)
        return p1 and p2 or p3

    def __repr__(self):
        p1 = "Iff(" + repr(self.left)
        p2 = repr(self.right) + ")"
        sol = p1 + ", " + p2
        return sol

    def __hash__(self):
        return hash((type(self).__name__, self.hashable))

    def atom_names(self):
        l = self.left.atom_names()
        r = self.right.atom_names()
        sol = l.union(r)
        return sol

    def evaluate(self, assignment):
        r = self.right.evaluate(assignment)
        l = self.left.evaluate(assignment)
        if (not l or r) and (not r or l):
            return True
        return False

    def to_cnf(self):
        r = self.right
        l = self.left
        sol = And(Or(Not(l), r), Or(Not(r), l)).to_cnf()
        return sol


def satisfying_assignments(expr):
    l = list(expr.atom_names())
    assign = {a: False for a in l}

    for i in range(0, pow(2, len(l))):
        pos = 0
        assign = copy.deepcopy(assign)
        for a in l:
            if i != 0:
                if i % pow(2, pos) == 0:
                    assign[a] = not assign[a]
            pos = pos + 1

        if expr.evaluate(assign):
            yield assign


class KnowledgeBase(object):
    def __init__(self):
        self.facts = set()

    def get_facts(self):
        return self.facts

    def tell(self, expr):
        excnf = expr.to_cnf()
        if type(excnf) == And:
            for i in excnf.conjuncts:
                self.facts.add(i)
        else:
            self.facts.add(excnf)

    def ask(self, expr):
        negation = Not(expr)
        current_facts = self.get_facts()
        assumption = And(*current_facts, negation).to_cnf()
        try:
            next(satisfying_assignments(assumption))
        except:
            return True
        return False


#TESTING
# Function 1
#print(Atom("a") == Atom("a"))
#print(Atom("a") == Atom("b"))

#Function 2
#a, b, c = map(Atom, 'abc')
#print(Implies(a,Iff(b,c)))

#Function 2 pt2
#a, b, c = map(Atom, "abc")
#print(And(a, Or(Not(b), c)))

#Function 3
#print(Atom("a").atom_names())

#Function 4
#e = Implies(Atom("a"), Atom("b"))
#print(e.evaluate({"a":False, "b": True}))
#print(e.evaluate({"a":True, "b": False}))

#Function 5
#e = Implies(Atom("a"), Atom("b"))
#a = satisfying_assignments(e)
#print(next(a))
#print(next(a))
#print(next(a))

#Function 5 part 2
#e = Iff(Iff(Atom("a"), Atom("b")), Atom("c"))
#print(list(satisfying_assignments(e)))

#Function 6
#print(Atom("a").to_cnf())
#a, b, c = map(Atom, "abc")
#print(Iff(a, Or(b,c)).to_cnf())

#Function 6 pt 2
a, b, c, d = map(Atom, "abcd")
print(Or(And(a, b), And(c, d)).to_cnf())

#Function 7
#a, b, c = map(Atom, "abc")
#kb = KnowledgeBase()
#kb.tell(a)
#kb.tell(Implies(a,b))
#print(kb.get_facts())
#print([kb.ask(x) for x in (a,b,c)])

#Function 7 part 2
#a, b, c = map(Atom, "abc")
#kb = KnowledgeBase()
#kb.tell(Iff(a, Or(b, c)))
#kb.tell(Not(a))
#print([kb.ask(x) for x in (a, Not(a))])
#print([kb.ask(x) for x in (b, Not(b))])
#print([kb.ask(x) for x in (c, Not(c))])

############################################################
# Section 2: Logic Puzzles
############################################################

# Puzzle 1

# Populate the knowledge base using statements of the form kb1.tell(...)

kb1 = KnowledgeBase()

myth = Atom("mythical")
mor = Atom("mortal")
mam = Atom("mammal")
horn = Atom("horned")
magic = Atom("magical")


kb1.tell(Implies(myth, Not(mor))) #if mythical then mortal
kb1.tell(Implies(Not(myth), And(mor, mam))) #if not mythical, then mortal
kb1.tell(Implies(Or(mor, mam), horn)) # if mammal or immortal, then horned
kb1.tell(Implies(horn, magic)) #the unicorn is magical  if it is horned

# Write an Expr for each query that should be asked of the knowledge base
mythical_query = kb1.ask(myth)
magical_query = kb1.ask(magic)
horned_query = kb1.ask(horn)

#print(kb1.get_facts())
#print(mythical_query)
#print(magical_query)
#print(horned_query)

# Record your answers as True or False; if you wish to use the above queries,
# they should not be run when this file is loaded
is_mythical = False
is_magical = True
is_horned = True

# Puzzle 2

# Write an Expr of the form And(...) encoding the constraints
Ann = Atom("a")
John = Atom("j")
Mary = Atom("m")

party_constraints = And(Implies(Or(Ann, Mary), John),
                        Implies(Not(Mary), Ann),
                        Implies(Ann, Not(John)))

# Compute a list of the valid attendance scenarios using a call to
# satisfying_assignments(expr)
valid_scenarios = list(satisfying_assignments(party_constraints))

#for s in valid_scenarios:
  #  print(s)

# Write your answer to the question in the assignment
puzzle_2_question = """
Both John and Mary will come but Ann will not come. 
"""

# Puzzle 3

# Populate the knowledge base using statements of the form kb3.tell(...)
kb3 = KnowledgeBase()

prize1 = Atom("p1")
prize2 = Atom("p2")
empty1 = Atom("e1")
empty2 = Atom("e2")
sign1 = Atom("s1")
sign2 = Atom("s2")

kb3.tell(Iff(prize1, Not(empty1)))
kb3.tell(Iff(prize2, Not(empty2)))
kb3.tell(Iff(And(prize1, empty2), sign1))
kb3.tell(Iff(Or(And(prize1, empty2),
                And(empty1, prize2)), sign2))
kb3.tell(And(Or(sign1, sign2),
             Or(Not(sign1),
                Not(sign2))))

#for query in [p1, p2, e1, e2, s1, s2]:
#   print ("query{}: {}".format(query, kb3.ask(query)))

# Write your answer to the question in the assignment; the queries you make
# should not be run when this file is loaded
puzzle_3_question = """
Sign on door 2 is true. Second room contains the prize and first room is empty.
"""

# Puzzle 4

# Populate the knowledge base using statements of the form kb4.tell(...)
kb4 = KnowledgeBase()

Adams = Atom("ia")
Brown = Atom("ib")
Clark = Atom("ic")
A = Atom("ka")
B = Atom("kb")
C = Atom("kc")

kb4.tell(Or(And(Adams, Brown, Not(Clark)),
            And(Adams, Not(Brown), Clark),
            And(Not(Adams), Brown, Clark)))
kb4.tell(Implies(Adams, B))
kb4.tell(Implies(Brown, Not(B)))
kb4.tell(Implies(Clark, And(A,B)))

#for query in [Adams, Brown, Clark, A, B, C]:
#   print("query{}: {}".format(query, kb4.ask(query)))

# Uncomment the line corresponding to the guilty suspect
# guilty_suspect = "Adams"
guilty_suspect = "Brown"
# guilty_suspect = "Clark"

# Describe the queries you made to ascertain your findings
puzzle_4_question = """
I use knowledge base to see who is innocent between the three -> Adams, Brown and Clark
False means the person is guilty. True means the person is innocent.
The man who is guilty is Brown who also lies. Adams and Clark are innocent and say the truth.
"""

############################################################
# Section 3: Feedback
############################################################

feedback_question_1 = """
I took around 16 hours on this assignment
"""

feedback_question_2 = """
The logic the to_cnf function were hard to write. 
"""

feedback_question_3 = """
I liked the idea of this assignment and how we're coding out all the propositional logic. 
"""
