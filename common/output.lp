\* assign_students_to_projects *\
Maximize
OBJ: s1p1IF + s1p1N + 0 s1p2IF + 0 s1p2N + 0 s1p3IF + 0 s1p3N + s2p1IF + s2p1N
 + 0 s2p2IF + 0 s2p2N + 0 s2p3IF + 0 s2p3N + s3p1IF + s3p1N + 0 s3p2IF
 + 0 s3p2N + 0 s3p3IF + 0 s3p3N + s4p1IF + s4p1N + s4p2IF + s4p2N + 0 s4p3IF
 + 0 s4p3N
Subject To
_C1: s1p1N + s1p2N + s1p3N <= 1
_C10: s1p2IF + s1p2N + s2p2IF + s2p2N + s3p2IF + s3p2N + s4p2IF + s4p2N <= 7
_C11: s1p3IF + s1p3N + s2p3IF + s2p3N + s3p3IF + s3p3N + s4p3IF + s4p3N <= 7
_C12: - 99999 b0 + s1p1IF + s1p1N + s2p1IF + s2p1N + s3p1IF + s3p1N + s4p1IF
 + s4p1N <= 0
_C13: - 99999 b1 + s1p2IF + s1p2N + s2p2IF + s2p2N + s3p2IF + s3p2N + s4p2IF
 + s4p2N <= 0
_C14: - 99999 b2 + s1p3IF + s1p3N + s2p3IF + s2p3N + s3p3IF + s3p3N + s4p3IF
 + s4p3N <= 0
_C15: - 3 b0 + s1p1IF + s1p1N + s2p1IF + s2p1N + s3p1IF + s3p1N + s4p1IF
 + s4p1N >= 0
_C16: - 3 b1 + s1p2IF + s1p2N + s2p2IF + s2p2N + s3p2IF + s3p2N + s4p2IF
 + s4p2N >= 0
_C17: - 3 b2 + s1p3IF + s1p3N + s2p3IF + s2p3N + s3p3IF + s3p3N + s4p3IF
 + s4p3N >= 0
_C18: s1p1IF + s2p1IF + s3p1IF + s4p1IF <= 2
_C19: s1p2IF + s2p2IF + s3p2IF + s4p2IF <= 2
_C2: s2p1N + s2p2N + s2p3N <= 1
_C20: s1p3IF + s2p3IF + s3p3IF + s4p3IF <= 2
_C3: s3p1N + s3p2N + s3p3N <= 1
_C4: s4p1N + s4p2N + s4p3N <= 1
_C5: s1p1IF + s1p2IF + s1p3IF <= 1
_C6: s2p1IF + s2p2IF + s2p3IF <= 1
_C7: s3p1IF + s3p2IF + s3p3IF <= 1
_C8: s4p1IF + s4p2IF + s4p3IF <= 1
_C9: s1p1IF + s1p1N + s2p1IF + s2p1N + s3p1IF + s3p1N + s4p1IF + s4p1N <= 7
Binaries
b0
b1
b2
s1p1IF
s1p1N
s1p2IF
s1p2N
s1p3IF
s1p3N
s2p1IF
s2p1N
s2p2IF
s2p2N
s2p3IF
s2p3N
s3p1IF
s3p1N
s3p2IF
s3p2N
s3p3IF
s3p3N
s4p1IF
s4p1N
s4p2IF
s4p2N
s4p3IF
s4p3N
End
