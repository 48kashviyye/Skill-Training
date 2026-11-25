# a = "Happy Birthday"
# print(a[-4:-7:-1]) 

# def convert(s, out):
#     out=''
#     for i in s:
#         if 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=i
#     return out
# print(convert(input("Enter a string: "), ''))

# def convert():
#     out=''
#     for i in s:
#         if 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=i
#     return out
# print(convert(input("Enter a string: "), ''))

# def convert(s, out):
#     out=''
#     for i in s:
#         if 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=i
# print(convert(input("Enter a string: "), ''))

# def convert():
#     out=''
#     for i in s:
#         if 'a'<=i<='z':
#             out+=chr(ord(i)-32)
#         else:
#             out+=i
#             print(out)
# print(convert(input("Enter a string: "), ''))

# class college:
#     cname="GCEM"
#     cloc='Hoodi'
# s1=college()
# print(s1.cname,s1.cloc)
# print(college.cname)

# s1=college()
# s1.sname='Harish'
# s1.phno=8296241254

# s2=college()
# s2.sname='Kashvi'

class college:
    def __init__(self, name, phno, usn):
        self.name = name
        self.phno = phno
        self.usn = usn
    def display(self):
        print(self.name, self.phno, self.usn)

s1=college('Kashvi', 8296241254, "1GD25CD022")
s2=college('Saurav', 8431760154, "1GD25IS046")

s1.display()
s2.display()