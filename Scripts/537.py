class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a1 = a.split("+")
        b1 = b.split("+")
        a_real = int(a1[0])
        a_complex = int(a1[1].replace("i",""))
        b_real = int(b1[0])
        b_complex = int(b1[1].replace("i",""))
        return "{}+{}i".format(a_real * b_real - a_complex * b_complex, a_real * b_complex + b_real * a_complex   )