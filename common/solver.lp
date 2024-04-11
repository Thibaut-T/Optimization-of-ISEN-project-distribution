\* assign_students_to_projects *\
Maximize
OBJ: 0 s10p10N + 0 s10p11N + 0 s10p12N + 0 s10p13N + 0 s10p14N + 0 s10p15N
 + 0 s10p1N + 0 s10p2N + 3 s10p3N + 4 s10p4N + 0 s10p5N + 5 s10p6N + 2 s10p7N
 + 4 s10p8N + 0 s10p9N + 0 s1p10N + 0 s1p11N + 0 s1p12N + 5 s1p13N + 5 s1p14N
 + 0 s1p15N + 0 s1p2N + 0 s1p3N + 0 s1p4N + 5 s1p5N + 0 s1p6N + 5 s1p7N
 + 5 s1p8N + 0 s1p9N + 0 s2p10N + 5 s2p11N + 0 s2p12N + 0 s2p13N + 0 s2p14N
 + 5 s2p15N + 0 s2p1N + 5 s2p2N + 0 s2p3N + 5 s2p4N + 0 s2p5N + 5 s2p6N
 + 0 s2p7N + 0 s2p8N + 0 s2p9N + 5 s3p10N + 5 s3p11N + 5 s3p12N + 0 s3p13N
 + 5 s3p14N + 0 s3p15N + 0 s3p1N + 5 s3p2N + 0 s3p3N + 0 s3p4N + 0 s3p5N
 + 0 s3p6N + 0 s3p7N + 0 s3p8N + 0 s3p9N + 0 s4p10N + 0 s4p11N + 0 s4p12N
 + 0 s4p13N + 5 s4p14N + 0 s4p15N + 0 s4p1N + 5 s4p2N + 5 s4p3N + 0 s4p4N
 + 0 s4p5N + 5 s4p6N + 5 s4p7N + 0 s4p8N + 0 s4p9N + 0 s5p10N + 0 s5p11N
 + 5 s5p12N + 0 s5p13N + 0 s5p14N + 0 s5p15N + 0 s5p1N + 5 s5p2N + 5 s5p3N
 + 5 s5p4N + 0 s5p5N + 0 s5p6N + 0 s5p7N + 5 s5p8N + 5 s5p9N + 0 s6p10N
 + 5 s6p11N + 5 s6p12N + 0 s6p13N + 0 s6p14N + 0 s6p15N + 0 s6p1N + 0 s6p2N
 + 5 s6p3N + 0 s6p4N + 0 s6p5N + 0 s6p6N + 0 s6p7N + 5 s6p8N + 5 s6p9N
 + 0 s7p10N + 5 s7p11N + 5 s7p12N + 0 s7p13N + 0 s7p14N + 5 s7p15N + 0 s7p1N
 + 0 s7p2N + 5 s7p3N + 5 s7p4N + 5 s7p5N + 0 s7p6N + 0 s7p7N + 0 s7p8N
 + 0 s7p9N + 0 s8p10N + 0 s8p11N + 0 s8p12N + 5 s8p13N + 0 s8p14N + 0 s8p15N
 + 5 s8p1N + 0 s8p2N + 5 s8p3N + 0 s8p4N + 5 s8p5N + 5 s8p6N + 0 s8p7N
 + 5 s8p8N + 0 s8p9N + 0 s9p10N + 0 s9p11N + 0 s9p12N + 0 s9p13N + 0 s9p14N
 + 0 s9p15N + 0 s9p1N + 0 s9p2N + 3 s9p3N + 4 s9p4N + 0 s9p5N + 5 s9p6N
 + 2 s9p7N + 4 s9p8N + 0 s9p9N
Subject To
_C1: s1p10N + s1p11N + s1p12N + s1p13N + s1p14N + s1p15N + s1p1N + s1p2N
 + s1p3N + s1p4N + s1p5N + s1p6N + s1p7N + s1p8N + s1p9N <= 1
_C10: s10p10N + s10p11N + s10p12N + s10p13N + s10p14N + s10p15N + s10p1N
 + s10p2N + s10p3N + s10p4N + s10p5N + s10p6N + s10p7N + s10p8N + s10p9N <= 1
_C11: s10p1N + s1p1N + s2p1N + s3p1N + s4p1N + s5p1N + s6p1N + s7p1N + s8p1N
 + s9p1N <= 4
_C12: s10p2N + s1p2N + s2p2N + s3p2N + s4p2N + s5p2N + s6p2N + s7p2N + s8p2N
 + s9p2N <= 7
_C13: s10p3N + s1p3N + s2p3N + s3p3N + s4p3N + s5p3N + s6p3N + s7p3N + s8p3N
 + s9p3N <= 7
_C14: s10p4N + s1p4N + s2p4N + s3p4N + s4p4N + s5p4N + s6p4N + s7p4N + s8p4N
 + s9p4N <= 4
_C15: s10p5N + s1p5N + s2p5N + s3p5N + s4p5N + s5p5N + s6p5N + s7p5N + s8p5N
 + s9p5N <= 3
_C16: s10p6N + s1p6N + s2p6N + s3p6N + s4p6N + s5p6N + s6p6N + s7p6N + s8p6N
 + s9p6N <= 4
_C17: s10p7N + s1p7N + s2p7N + s3p7N + s4p7N + s5p7N + s6p7N + s7p7N + s8p7N
 + s9p7N <= 4
_C18: s10p8N + s1p8N + s2p8N + s3p8N + s4p8N + s5p8N + s6p8N + s7p8N + s8p8N
 + s9p8N <= 4
_C19: s10p9N + s1p9N + s2p9N + s3p9N + s4p9N + s5p9N + s6p9N + s7p9N + s8p9N
 + s9p9N <= 4
_C2: s2p10N + s2p11N + s2p12N + s2p13N + s2p14N + s2p15N + s2p1N + s2p2N
 + s2p3N + s2p4N + s2p5N + s2p6N + s2p7N + s2p8N + s2p9N <= 1
_C20: s10p10N + s1p10N + s2p10N + s3p10N + s4p10N + s5p10N + s6p10N + s7p10N
 + s8p10N + s9p10N <= 3
_C21: s10p11N + s1p11N + s2p11N + s3p11N + s4p11N + s5p11N + s6p11N + s7p11N
 + s8p11N + s9p11N <= 3
_C22: s10p12N + s1p12N + s2p12N + s3p12N + s4p12N + s5p12N + s6p12N + s7p12N
 + s8p12N + s9p12N <= 5
_C23: s10p13N + s1p13N + s2p13N + s3p13N + s4p13N + s5p13N + s6p13N + s7p13N
 + s8p13N + s9p13N <= 7
_C24: s10p14N + s1p14N + s2p14N + s3p14N + s4p14N + s5p14N + s6p14N + s7p14N
 + s8p14N + s9p14N <= 5
_C25: s10p15N + s1p15N + s2p15N + s3p15N + s4p15N + s5p15N + s6p15N + s7p15N
 + s8p15N + s9p15N <= 6
_C26: - 99999 b0 + s10p1N + s1p1N + s2p1N + s3p1N + s4p1N + s5p1N + s6p1N
 + s7p1N + s8p1N + s9p1N <= 0
_C27: - 99999 b1 + s10p2N + s1p2N + s2p2N + s3p2N + s4p2N + s5p2N + s6p2N
 + s7p2N + s8p2N + s9p2N <= 0
_C28: - 99999 b2 + s10p3N + s1p3N + s2p3N + s3p3N + s4p3N + s5p3N + s6p3N
 + s7p3N + s8p3N + s9p3N <= 0
_C29: - 99999 b3 + s10p4N + s1p4N + s2p4N + s3p4N + s4p4N + s5p4N + s6p4N
 + s7p4N + s8p4N + s9p4N <= 0
_C3: s3p10N + s3p11N + s3p12N + s3p13N + s3p14N + s3p15N + s3p1N + s3p2N
 + s3p3N + s3p4N + s3p5N + s3p6N + s3p7N + s3p8N + s3p9N <= 1
_C30: - 99999 b4 + s10p5N + s1p5N + s2p5N + s3p5N + s4p5N + s5p5N + s6p5N
 + s7p5N + s8p5N + s9p5N <= 0
_C31: - 99999 b5 + s10p6N + s1p6N + s2p6N + s3p6N + s4p6N + s5p6N + s6p6N
 + s7p6N + s8p6N + s9p6N <= 0
_C32: - 99999 b6 + s10p7N + s1p7N + s2p7N + s3p7N + s4p7N + s5p7N + s6p7N
 + s7p7N + s8p7N + s9p7N <= 0
_C33: - 99999 b7 + s10p8N + s1p8N + s2p8N + s3p8N + s4p8N + s5p8N + s6p8N
 + s7p8N + s8p8N + s9p8N <= 0
_C34: - 99999 b8 + s10p9N + s1p9N + s2p9N + s3p9N + s4p9N + s5p9N + s6p9N
 + s7p9N + s8p9N + s9p9N <= 0
_C35: - 99999 b9 + s10p10N + s1p10N + s2p10N + s3p10N + s4p10N + s5p10N
 + s6p10N + s7p10N + s8p10N + s9p10N <= 0
_C36: - 99999 b10 + s10p11N + s1p11N + s2p11N + s3p11N + s4p11N + s5p11N
 + s6p11N + s7p11N + s8p11N + s9p11N <= 0
_C37: - 99999 b11 + s10p12N + s1p12N + s2p12N + s3p12N + s4p12N + s5p12N
 + s6p12N + s7p12N + s8p12N + s9p12N <= 0
_C38: - 99999 b12 + s10p13N + s1p13N + s2p13N + s3p13N + s4p13N + s5p13N
 + s6p13N + s7p13N + s8p13N + s9p13N <= 0
_C39: - 99999 b13 + s10p14N + s1p14N + s2p14N + s3p14N + s4p14N + s5p14N
 + s6p14N + s7p14N + s8p14N + s9p14N <= 0
_C4: s4p10N + s4p11N + s4p12N + s4p13N + s4p14N + s4p15N + s4p1N + s4p2N
 + s4p3N + s4p4N + s4p5N + s4p6N + s4p7N + s4p8N + s4p9N <= 1
_C40: - 99999 b14 + s10p15N + s1p15N + s2p15N + s3p15N + s4p15N + s5p15N
 + s6p15N + s7p15N + s8p15N + s9p15N <= 0
_C41: - 3 b0 + s10p1N + s1p1N + s2p1N + s3p1N + s4p1N + s5p1N + s6p1N + s7p1N
 + s8p1N + s9p1N >= 0
_C42: - 3 b1 + s10p2N + s1p2N + s2p2N + s3p2N + s4p2N + s5p2N + s6p2N + s7p2N
 + s8p2N + s9p2N >= 0
_C43: - 3 b2 + s10p3N + s1p3N + s2p3N + s3p3N + s4p3N + s5p3N + s6p3N + s7p3N
 + s8p3N + s9p3N >= 0
_C44: - 3 b3 + s10p4N + s1p4N + s2p4N + s3p4N + s4p4N + s5p4N + s6p4N + s7p4N
 + s8p4N + s9p4N >= 0
_C45: - 2 b4 + s10p5N + s1p5N + s2p5N + s3p5N + s4p5N + s5p5N + s6p5N + s7p5N
 + s8p5N + s9p5N >= 0
_C46: - 3 b5 + s10p6N + s1p6N + s2p6N + s3p6N + s4p6N + s5p6N + s6p6N + s7p6N
 + s8p6N + s9p6N >= 0
_C47: - 3 b6 + s10p7N + s1p7N + s2p7N + s3p7N + s4p7N + s5p7N + s6p7N + s7p7N
 + s8p7N + s9p7N >= 0
_C48: - 4 b7 + s10p8N + s1p8N + s2p8N + s3p8N + s4p8N + s5p8N + s6p8N + s7p8N
 + s8p8N + s9p8N >= 0
_C49: - b8 + s10p9N + s1p9N + s2p9N + s3p9N + s4p9N + s5p9N + s6p9N + s7p9N
 + s8p9N + s9p9N >= 0
_C5: s5p10N + s5p11N + s5p12N + s5p13N + s5p14N + s5p15N + s5p1N + s5p2N
 + s5p3N + s5p4N + s5p5N + s5p6N + s5p7N + s5p8N + s5p9N <= 1
_C50: - 3 b9 + s10p10N + s1p10N + s2p10N + s3p10N + s4p10N + s5p10N + s6p10N
 + s7p10N + s8p10N + s9p10N >= 0
_C51: - 2 b10 + s10p11N + s1p11N + s2p11N + s3p11N + s4p11N + s5p11N + s6p11N
 + s7p11N + s8p11N + s9p11N >= 0
_C52: - 3 b11 + s10p12N + s1p12N + s2p12N + s3p12N + s4p12N + s5p12N + s6p12N
 + s7p12N + s8p12N + s9p12N >= 0
_C53: - 6 b12 + s10p13N + s1p13N + s2p13N + s3p13N + s4p13N + s5p13N + s6p13N
 + s7p13N + s8p13N + s9p13N >= 0
_C54: - 3 b13 + s10p14N + s1p14N + s2p14N + s3p14N + s4p14N + s5p14N + s6p14N
 + s7p14N + s8p14N + s9p14N >= 0
_C55: - 5 b14 + s10p15N + s1p15N + s2p15N + s3p15N + s4p15N + s5p15N + s6p15N
 + s7p15N + s8p15N + s9p15N >= 0
_C56: s10p2N = 1
_C6: s6p10N + s6p11N + s6p12N + s6p13N + s6p14N + s6p15N + s6p1N + s6p2N
 + s6p3N + s6p4N + s6p5N + s6p6N + s6p7N + s6p8N + s6p9N <= 1
_C7: s7p10N + s7p11N + s7p12N + s7p13N + s7p14N + s7p15N + s7p1N + s7p2N
 + s7p3N + s7p4N + s7p5N + s7p6N + s7p7N + s7p8N + s7p9N <= 1
_C8: s8p10N + s8p11N + s8p12N + s8p13N + s8p14N + s8p15N + s8p1N + s8p2N
 + s8p3N + s8p4N + s8p5N + s8p6N + s8p7N + s8p8N + s8p9N <= 1
_C9: s9p10N + s9p11N + s9p12N + s9p13N + s9p14N + s9p15N + s9p1N + s9p2N
 + s9p3N + s9p4N + s9p5N + s9p6N + s9p7N + s9p8N + s9p9N <= 1
Binaries
b0
b1
b10
b11
b12
b13
b14
b2
b3
b4
b5
b6
b7
b8
b9
s10p10N
s10p11N
s10p12N
s10p13N
s10p14N
s10p15N
s10p1N
s10p2N
s10p3N
s10p4N
s10p5N
s10p6N
s10p7N
s10p8N
s10p9N
s1p10N
s1p11N
s1p12N
s1p13N
s1p14N
s1p15N
s1p1N
s1p2N
s1p3N
s1p4N
s1p5N
s1p6N
s1p7N
s1p8N
s1p9N
s2p10N
s2p11N
s2p12N
s2p13N
s2p14N
s2p15N
s2p1N
s2p2N
s2p3N
s2p4N
s2p5N
s2p6N
s2p7N
s2p8N
s2p9N
s3p10N
s3p11N
s3p12N
s3p13N
s3p14N
s3p15N
s3p1N
s3p2N
s3p3N
s3p4N
s3p5N
s3p6N
s3p7N
s3p8N
s3p9N
s4p10N
s4p11N
s4p12N
s4p13N
s4p14N
s4p15N
s4p1N
s4p2N
s4p3N
s4p4N
s4p5N
s4p6N
s4p7N
s4p8N
s4p9N
s5p10N
s5p11N
s5p12N
s5p13N
s5p14N
s5p15N
s5p1N
s5p2N
s5p3N
s5p4N
s5p5N
s5p6N
s5p7N
s5p8N
s5p9N
s6p10N
s6p11N
s6p12N
s6p13N
s6p14N
s6p15N
s6p1N
s6p2N
s6p3N
s6p4N
s6p5N
s6p6N
s6p7N
s6p8N
s6p9N
s7p10N
s7p11N
s7p12N
s7p13N
s7p14N
s7p15N
s7p1N
s7p2N
s7p3N
s7p4N
s7p5N
s7p6N
s7p7N
s7p8N
s7p9N
s8p10N
s8p11N
s8p12N
s8p13N
s8p14N
s8p15N
s8p1N
s8p2N
s8p3N
s8p4N
s8p5N
s8p6N
s8p7N
s8p8N
s8p9N
s9p10N
s9p11N
s9p12N
s9p13N
s9p14N
s9p15N
s9p1N
s9p2N
s9p3N
s9p4N
s9p5N
s9p6N
s9p7N
s9p8N
s9p9N
End
