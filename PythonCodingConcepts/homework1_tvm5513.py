###########################################################
# CMPSC 442: Homework 1
############################################################

student_name = "Trisha Mandal"

############################################################
# Section 1: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    #if inside a for loop to use the function
    return [f(value) for value in l if p(value)]

def concatenate(seqs):
    #using a double for loop to concatenate sequenceS
    return [value for sequence in seqs for value in sequence]

def transpose(matrix):
    #first finding the number of rows and columns and
    #then using a double for loop to switch the rows and columns
    result = []
    row = len(matrix)
    column = len(matrix[0])
    for i in range(0,column):
        temp = []
        for j in range(0,row):
            temp.append(matrix[j][i])
        result.append(temp)
    return result

############################################################
# Section 2: Sequence Slicing
############################################################

# I used slices notation for lists in python to do the three following functions
def copy(seq):
    return seq[:]

def all_but_last(seq):
    return seq[:-1]

def every_other(seq):
    return seq[::2]

############################################################
# Section 3: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for a in range(0,len(seq) + 1):
        yield seq[:a]

def suffixes(seq):
    for a in range(0,len(seq) + 1):
        yield seq[a:]

def slices(seq):
    for a in range(0,len(seq)+1):
        for b in range(a+1, len(seq)+1):
                yield seq[a:b]

############################################################
# Section 4: Text Processing
############################################################

def normalize(text):
    solution = " ".join(text.lower().split())
    return solution

#I am checking if the character from the string is not a vowel and then
# I am concatenating the string to the new word
def no_vowels(text):
    solution = ""
    for ch in text:
        if ch not in "AEIOUaeiou":
            solution += ch
    return solution

#I made a dictionary to save the digits in words. Then I am checking
#if the string has characters which are the numbers and then I am printing them
#out as words
def digits_to_words(text):
    solution = ""
    digits = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    for ch in text:
        if ch in "0123456789":
            solution = solution + digits[int(ch)] + " "
    solution = solution.strip()
    return solution

def to_mixed_case(name):
    s = ""
    for part in name.split("_"):
        if part != "":
            l = part.lower()
            s = s + "".join(l[0].upper() + l[1:])
    solution = s[0].lower() + s[1:]
    return solution

############################################################
# Section 5: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.tempPolynomial = polynomial

    def get_polynomial(self):
        return tuple(self.tempPolynomial)

    def __neg__(self):
        solution = Polynomial([(-value[0],value[1]) for value in self.tempPolynomial])
        return solution

    def __add__(self, other):
        solution = Polynomial(list(self.get_polynomial())+list(other.get_polynomial()))
        return solution

    def __sub__(self, other):
        solution = (self+(-other))
        return solution

    def __mul__(self, other):
        newpolynomial = []
        for coefficient1, index1 in self.tempPolynomial:
            for coefficient2, index2 in other.tempPolynomial:
               newpolynomial.append((coefficient1 * coefficient2, index1 + index2))
        return Polynomial(newpolynomial)

    def __call__(self, x):
        solution = sum([coefficient * x**index for coefficient,index in self.tempPolynomial])
        return solution

    def simplify(self):
        pass

    def __str__(self):
        tempstr = ""
        for i in self.tempPolynomial:
            if i[0] == 1 and i[1] == 0:
                put = "+ 1 "
            elif i[0] == -1 and i[1] == 0:
                put = "- 1 "
            else:
                if i[0] == 1:
                    put = '+ '
                elif i[0] == -1:
                    put = "- "
                elif i[0] < 0:
                    put = "- " + str(abs(i[0]))
                else:
                    put = "+ " + str(i[0])

                if i[1] == 1:
                    put = put + "x "
                elif i[1] == 0:
                    put = put + " "
                else:
                    put = put + "x" + "^" + str(i[1]) + " "
            tempstr = tempstr + put
        if tempstr[0] == "+":
            return (tempstr[2:-1])
        else:
            return ("-" + tempstr[2:-1])

############################################################
# Section 6: Feedback
############################################################

feedback_question_1 = """
I spent around 14.0 hours to do this assignment
"""

feedback_question_2 = """
I think the polynomial function was very hard for me to come up with.
the simplify and str functions itself took me 8 hours. I could not even complete simplify.
I was also not very sure about the yield functions.
"""

feedback_question_3 = """
I liked the fact that I got to learn about new functions and notations in Python through this assignment.
I feel like this assigment was a bit overwelming for me as Python is new to me
and I think a lot of people like me would agree. 
Maybe a little bit less difficulty for the first assignment would be better.
"""