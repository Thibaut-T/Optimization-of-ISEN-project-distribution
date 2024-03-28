\* assign_students_to_projects *\
Maximize
OBJ: 7 s1p1IF + 7 s1p1N + 0 s1p2IF + 0 s1p2N + 9 s1p3IF + 9 s1p3N + 0 s1p4IF
 + 0 s1p4N + 8 s1p5IF + 8 s1p5N + 10 s1p6IF + 10 s1p6N + 0 s1p7IF + 0 s1p7N
 + 7 s1p8IF + 7 s1p8N + 8 s1p9IF + 8 s1p9N + 0 s2p1N + 0 s2p2N + 0 s2p3N
 + 0 s2p4N + 5 s2p5N + 6 s2p6N + 7 s2p7N + 8 s2p8N + 5 s2p9N + 0 s3p1N
 + 5 s3p2N + 3 s3p3N + 0 s3p4N + 6 s3p5N + 0 s3p6N + 0 s3p7N + 0 s3p8N
 + 5 s3p9N
Subject To
_C1: s1p1N + s1p2N + s1p3N + s1p4N + s1p5N + s1p6N + s1p7N + s1p8N + s1p9N
 <= 1
_C10: s1p6IF + s1p6N + s2p6N + s3p6N <= 7
_C11: s1p7IF + s1p7N + s2p7N + s3p7N <= 7
_C12: s1p8IF + s1p8N + s2p8N + s3p8N <= 7
_C13: s1p9IF + s1p9N + s2p9N + s3p9N <= 7
_C14: - 99999 b0 + s1p1IF + s1p1N + s2p1N + s3p1N <= 0
_C15: - 99999 b1 + s1p2IF + s1p2N + s2p2N + s3p2N <= 0
_C16: - 99999 b2 + s1p3IF + s1p3N + s2p3N + s3p3N <= 0
_C17: - 99999 b3 + s1p4IF + s1p4N + s2p4N + s3p4N <= 0
_C18: - 99999 b4 + s1p5IF + s1p5N + s2p5N + s3p5N <= 0
_C19: - 99999 b5 + s1p6IF + s1p6N + s2p6N + s3p6N <= 0
_C2: s2p1N + s2p2N + s2p3N + s2p4N + s2p5N + s2p6N + s2p7N + s2p8N + s2p9N
 <= 1
_C20: - 99999 b6 + s1p7IF + s1p7N + s2p7N + s3p7N <= 0
_C21: - 99999 b7 + s1p8IF + s1p8N + s2p8N + s3p8N <= 0
_C22: - 99999 b8 + s1p9IF + s1p9N + s2p9N + s3p9N <= 0
_C23: - 3 b0 + s1p1IF + s1p1N + s2p1N + s3p1N >= 0
_C24: - 3 b1 + s1p2IF + s1p2N + s2p2N + s3p2N >= 0
_C25: - 3 b2 + s1p3IF + s1p3N + s2p3N + s3p3N >= 0
_C26: - 3 b3 + s1p4IF + s1p4N + s2p4N + s3p4N >= 0
_C27: - 3 b4 + s1p5IF + s1p5N + s2p5N + s3p5N >= 0
_C28: - 3 b5 + s1p6IF + s1p6N + s2p6N + s3p6N >= 0
_C29: - 3 b6 + s1p7IF + s1p7N + s2p7N + s3p7N >= 0
_C3: s3p1N + s3p2N + s3p3N + s3p4N + s3p5N + s3p6N + s3p7N + s3p8N + s3p9N
 <= 1
_C30: - 3 b7 + s1p8IF + s1p8N + s2p8N + s3p8N >= 0
_C31: - 3 b8 + s1p9IF + s1p9N + s2p9N + s3p9N >= 0
_C32: s1p1IF <= 2
_C33: s1p2IF <= 2
_C34: s1p3IF <= 2
_C35: s1p4IF <= 2
_C36: s1p5IF <= 2
_C37: s1p6IF <= 2
_C38: s1p7IF <= 2
_C39: s1p8IF <= 2
_C4: s1p1IF + s1p2IF + s1p3IF + s1p4IF + s1p5IF + s1p6IF + s1p7IF + s1p8IF
 + s1p9IF <= 1
_C40: s1p9IF <= 2
_C5: s1p1IF + s1p1N + s2p1N + s3p1N <= 7
_C6: s1p2IF + s1p2N + s2p2N + s3p2N <= 7
_C7: s1p3IF + s1p3N + s2p3N + s3p3N <= 7
_C8: s1p4IF + s1p4N + s2p4N + s3p4N <= 7
_C9: s1p5IF + s1p5N + s2p5N + s3p5N <= 7
Binaries
b0
b1
b2
b3
b4
b5
b6
b7
b8
s1p1IF
s1p1N
s1p2IF
s1p2N
s1p3IF
s1p3N
s1p4IF
s1p4N
s1p5IF
s1p5N
s1p6IF
s1p6N
s1p7IF
s1p7N
s1p8IF
s1p8N
s1p9IF
s1p9N
s2p1N
s2p2N
s2p3N
s2p4N
s2p5N
s2p6N
s2p7N
s2p8N
s2p9N
s3p1N
s3p2N
s3p3N
s3p4N
s3p5N
s3p6N
s3p7N
s3p8N
s3p9N
End
