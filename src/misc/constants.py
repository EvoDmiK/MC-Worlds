from functools import partial

alphacolor = (0,0,0)

basecolors = [alphacolor, (127, 178, 56), (247, 233, 163), (199, 199, 199),
    (255, 0, 0), (160, 160, 255), (167, 167, 167), (0, 124, 0),
    (255, 255, 255), (164, 168, 184), (151, 109, 77), (112, 112, 112),
    (64, 64, 255), (143, 119, 72), (255, 252, 245), (216, 127, 51),
    (178, 76, 216), (102, 153, 216), (229, 229, 51), (127, 204, 25),
    (242, 127, 165), (76, 76, 76), (153, 153, 153), (76, 127, 153),
    (127, 63, 178), (51, 76, 178), (102, 76, 51), (102, 127, 51),
    (153, 51, 51), (25, 25, 25), (250, 238, 77), (92, 219, 213),
    (74, 128, 255), (0, 217, 58), (129, 86, 49), (112, 2, 0)]
    
allcolors = [alphacolor, alphacolor, alphacolor, alphacolor, (90, 126, 40),
    (110, 154, 48), (127, 178, 56), (67, 94, 30), (174, 164, 115),
    (213, 201, 141), (247, 233, 163), (131, 123, 86),
    (140, 140, 140), (172, 172, 172), (199, 199, 199),
    (105, 105, 105), (180, 0, 0), (220, 0, 0), (255, 0, 0),
    (135, 0, 0), (113, 113, 180), (138, 138, 220), (160, 160, 255),
    (85, 85, 135), (118, 118, 118), (144, 144, 144), (167, 167, 167),
    (88, 88, 88), (0, 88, 0), (0, 107, 0), (0, 124, 0), (0, 66, 0),
    (180, 180, 180), (220, 220, 220), (255, 255, 255), (135, 135, 135),
    (116, 119, 130), (141, 145, 159), (164, 168, 184), (87, 89, 97),
    (107, 77, 54), (130, 94, 66), (151, 109, 77), (80, 58, 41),
    (79, 79, 79), (97, 97, 97), (112, 112, 112), (59, 59, 59),
    (45, 45, 180), (55, 55, 220), (64, 64, 255), (34, 34, 135),
    (101, 84, 51), (123, 103, 62), (143, 119, 72), (76, 63, 38),
    (180, 178, 173), (220, 217, 211), (255, 252, 245),
    (135, 133, 130), (152, 90, 36), (186, 110, 44),
    (216, 127, 51), (114, 67, 27), (126, 54, 152),
    (154, 66, 186), (178, 76, 216), (94, 40, 114), (72, 108, 152),
    (88, 132, 186), (102, 153, 216), (54, 81, 114),
    (162, 162, 36), (198, 198, 44), (229, 229, 51),
    (121, 121, 27), (90, 144, 18), (110, 176, 22), (127, 204, 25),
    (67, 108, 13), (171, 90, 116), (209, 110, 142),
    (242, 127, 165), (128, 67, 87), (54, 54, 54), (66, 66, 66),
    (76, 76, 76), (40, 40, 40), (108, 108, 108), (132, 132, 132),
    (153, 153, 153), (81, 81, 81), (54, 90, 108), (66, 110, 132),
    (76, 127, 153), (40, 67, 81), (90, 44, 126), (110, 54, 154),
    (127, 63, 178), (67, 33, 94), (36, 54, 126), (44, 66, 154),
    (51, 76, 178), (27, 40, 94), (72, 54, 36), (88, 66, 44),
    (102, 76, 51), (54, 40, 27), (72, 90, 36), (88, 110, 44),
    (102, 127, 51), (54, 67, 27), (108, 36, 36), (132, 44, 44),
    (153, 51, 51), (81, 27, 27), (18, 18, 18), (22, 22, 22),
    (25, 25, 25), (13, 13, 13), (176, 168, 54), (216, 205, 66),
    (250, 238, 77), (132, 126, 41), (65, 155, 150),
    (79, 189, 184), (92, 219, 213), (49, 116, 113),
    (52, 90, 180), (64, 110, 220), (74, 128, 255), (39, 68, 135),
    (0, 153, 41), (0, 187, 50), (0, 217, 58), (0, 115, 31),
    (91, 61, 35), (111, 74, 42), (129, 86, 49), (68, 46, 26),
    (79, 1, 0), (97, 2, 0), (112, 2, 0), (59, 1, 0)]
        
allcolorsinversemap = {alphacolor: 3, (90, 126, 40): 4, (110, 154, 48): 5, 
    (127, 178, 56): 6, (67, 94, 30): 7, (174, 164, 115): 8,
    (213, 201, 141): 9, (247, 233, 163): 10, (131, 123, 86): 11, 
    (140, 140, 140): 12, (172, 172, 172): 13, (199, 199, 199): 14, 
    (105, 105, 105): 15, (180, 0, 0): 16, (220, 0, 0): 17, (255, 0, 0): 18, 
    (135, 0, 0): 19, (113, 113, 180): 20, (138, 138, 220): 21, 
    (160, 160, 255): 22, (85, 85, 135): 23, (118, 118, 118): 24, 
    (144, 144, 144): 25, (167, 167, 167): 26, (88, 88, 88): 27, 
    (0, 88, 0): 28, (0, 107, 0): 29, (0, 124, 0): 30, (0, 66, 0): 31, 
    (180, 180, 180): 32, (220, 220, 220): 33, (255, 255, 255): 34, 
    (135, 135, 135): 35, (116, 119, 130): 36, (141, 145, 159): 37, 
    (164, 168, 184): 38, (87, 89, 97): 39, (107, 77, 54): 40, 
    (130, 94, 66): 41, (151, 109, 77): 42, (80, 58, 41): 43, 
    (79, 79, 79): 44, (97, 97, 97): 45, (112, 112, 112): 46, 
    (59, 59, 59): 47, (45, 45, 180): 48, (55, 55, 220): 49, 
    (64, 64, 255): 50, (34, 34, 135): 51, (101, 84, 51): 52, 
    (123, 103, 62): 53, (143, 119, 72): 54, (76, 63, 38): 55, 
    (180, 178, 173): 56, (220, 217, 211): 57, (255, 252, 245): 58, 
    (135, 133, 130): 59, (152, 90, 36): 60, (186, 110, 44): 61, 
    (216, 127, 51): 62, (114, 67, 27): 63, (126, 54, 152): 64, 
    (154, 66, 186): 65, (178, 76, 216): 66, (94, 40, 114): 67, 
    (72, 108, 152): 68, (88, 132, 186): 69, (102, 153, 216): 70, 
    (54, 81, 114): 71, (162, 162, 36): 72, (198, 198, 44): 73, 
    (229, 229, 51): 74, (121, 121, 27): 75, (90, 144, 18): 76, 
    (110, 176, 22): 77, (127, 204, 25): 78, (67, 108, 13): 79, 
    (171, 90, 116): 80, (209, 110, 142): 81, (242, 127, 165): 82, 
    (128, 67, 87): 83, (54, 54, 54): 84, (66, 66, 66): 85, 
    (76, 76, 76): 86, (40, 40, 40): 87, (108, 108, 108): 88, 
    (132, 132, 132): 89, (153, 153, 153): 90, (81, 81, 81): 91, 
    (54, 90, 108): 92, (66, 110, 132): 93, (76, 127, 153): 94, 
    (40, 67, 81): 95, (90, 44, 126): 96, (110, 54, 154): 97, 
    (127, 63, 178): 98, (67, 33, 94): 99, (36, 54, 126): 100, 
    (44, 66, 154): 101, (51, 76, 178): 102, (27, 40, 94): 103, 
    (72, 54, 36): 104, (88, 66, 44): 105, (102, 76, 51): 106, 
    (54, 40, 27): 107, (72, 90, 36): 108, (88, 110, 44): 109, 
    (102, 127, 51): 110, (54, 67, 27): 111, (108, 36, 36): 112, 
    (132, 44, 44): 113, (153, 51, 51): 114, (81, 27, 27): 115, 
    (18, 18, 18): 116, (22, 22, 22): 117, (25, 25, 25): 118, 
    (13, 13, 13): 119, (176, 168, 54): 120, (216, 205, 66): 121, 
    (250, 238, 77): 122, (132, 126, 41): 123, (65, 155, 150): 124, 
    (79, 189, 184): 125, (92, 219, 213): 126, (49, 116, 113): 127, 
    (52, 90, 180): 128, (64, 110, 220): 129, (74, 128, 255): 130, 
    (39, 68, 135): 131, (0, 153, 41): 132, (0, 187, 50): 133, 
    (0, 217, 58): 134, (0, 115, 31): 135, (91, 61, 35): 136, 
    (111, 74, 42): 137, (129, 86, 49): 138, (68, 46, 26): 139, 
    (79, 1, 0): 140, (97, 2, 0): 141, (112, 2, 0): 142, (59, 1, 0): 143} 

estimationlookup = {
    10:
        [[[119, 117, 118, 103, 51, 51, 51, 48, 48, 49, 50], 
        [117, 118, 103, 103, 103, 51, 48, 48, 49, 49, 50], 
        [31, 87, 95, 103, 100, 131, 101, 48, 49, 49, 50], 
        [28, 135, 95, 95, 131, 131, 101, 128, 128, 50, 50], 
        [29, 135, 135, 127, 127, 127, 128, 128, 129, 129, 130], 
        [30, 132, 132, 127, 127, 127, 124, 128, 129, 129, 130], 
        [132, 132, 133, 133, 127, 124, 124, 124, 129, 130, 130], 
        [133, 133, 133, 133, 134, 124, 124, 125, 125, 125, 130], 
        [134, 134, 134, 134, 134, 124, 125, 125, 125, 126, 126], 
        [134, 134, 134, 134, 134, 134, 125, 125, 126, 126, 126], 
        [134, 134, 134, 134, 134, 134, 126, 126, 126, 126, 126]], 
        [[117, 118, 87, 103, 51, 51, 48, 48, 49, 49, 50], 
        [107, 87, 87, 103, 100, 51, 48, 48, 49, 49, 50], 
        [111, 111, 95, 95, 100, 131, 101, 102, 49, 50, 50], 
        [111, 111, 95, 95, 92, 131, 128, 128, 129, 50, 50], 
        [79, 7, 7, 127, 127, 127, 128, 128, 129, 129, 130], 
        [79, 132, 132, 127, 127, 124, 124, 129, 129, 130, 130], 
        [132, 132, 133, 127, 124, 124, 124, 125, 125, 130, 130], 
        [133, 133, 133, 133, 124, 124, 125, 125, 125, 126, 130], 
        [134, 134, 134, 134, 134, 125, 125, 125, 126, 126, 126], 
        [134, 134, 134, 134, 134, 125, 125, 126, 126, 126, 126], 
        [134, 134, 134, 134, 134, 125, 126, 126, 126, 126, 126]], 
        [[143, 115, 99, 99, 99, 51, 48, 48, 49, 49, 50], 
        [139, 107, 84, 99, 99, 96, 48, 48, 49, 50, 50], 
        [111, 55, 85, 86, 71, 101, 102, 102, 49, 50, 50], 
        [7, 108, 86, 91, 92, 23, 128, 128, 129, 50, 50], 
        [79, 7, 109, 127, 127, 93, 68, 129, 129, 130, 130], 
        [76, 4, 4, 127, 127, 124, 124, 69, 129, 130, 130], 
        [76, 76, 5, 127, 124, 124, 124, 125, 70, 130, 130], 
        [77, 77, 5, 124, 124, 124, 125, 125, 125, 126, 130], 
        [77, 77, 134, 134, 124, 125, 125, 125, 126, 126, 126], 
        [78, 134, 134, 134, 125, 125, 125, 126, 126, 126, 126], 
        [78, 134, 134, 134, 134, 125, 126, 126, 126, 126, 126]], 
        [[141, 115, 115, 99, 67, 96, 97, 48, 49, 50, 50], 
        [115, 115, 43, 99, 67, 96, 97, 97, 49, 50, 50], 
        [136, 136, 105, 91, 96, 23, 97, 98, 49, 50, 50], 
        [7, 108, 52, 27, 39, 23, 68, 20, 129, 50, 50], 
        [79, 109, 109, 45, 15, 68, 94, 69, 129, 130, 130], 
        [76, 4, 110, 15, 46, 94, 69, 69, 70, 130, 130], 
        [76, 5, 5, 5, 124, 124, 124, 125, 70, 70, 130], 
        [77, 77, 6, 6, 124, 124, 125, 125, 126, 126, 126], 
        [78, 78, 6, 6, 124, 125, 125, 126, 126, 126, 126], 
        [78, 78, 78, 6, 125, 125, 126, 126, 126, 126, 126], 
        [78, 78, 78, 78, 125, 126, 126, 126, 126, 126, 126]], 
        [[142, 112, 112, 67, 67, 96, 97, 98, 98, 50, 50], 
        [112, 112, 113, 83, 67, 97, 97, 98, 98, 50, 50], 
        [63, 137, 40, 83, 83, 97, 97, 98, 98, 50, 50], 
        [63, 137, 41, 45, 15, 23, 20, 20, 20, 130, 130], 
        [75, 75, 53, 11, 46, 36, 20, 20, 21, 21, 130], 
        [75, 5, 5, 11, 24, 89, 37, 69, 70, 70, 130], 
        [77, 5, 6, 6, 59, 12, 37, 70, 70, 70, 22], 
        [77, 78, 6, 6, 6, 90, 125, 125, 126, 126, 22], 
        [78, 78, 6, 6, 6, 125, 125, 126, 126, 126, 126], 
        [78, 78, 78, 6, 6, 125, 126, 126, 126, 126, 126], 
        [78, 78, 78, 78, 6, 126, 126, 126, 126, 126, 126]], 
        [[19, 113, 113, 114, 67, 64, 64, 98, 65, 66, 66], 
        [113, 113, 114, 83, 83, 64, 64, 98, 65, 66, 66], 
        [63, 114, 114, 83, 83, 64, 98, 65, 65, 66, 66], 
        [60, 60, 41, 83, 80, 80, 98, 65, 66, 66, 66], 
        [75, 123, 54, 11, 24, 89, 20, 20, 21, 21, 22], 
        [75, 123, 54, 11, 59, 12, 37, 21, 21, 21, 22], 
        [72, 72, 6, 6, 8, 90, 37, 38, 21, 22, 22], 
        [78, 78, 6, 6, 8, 90, 26, 38, 38, 22, 22], 
        [78, 78, 6, 6, 8, 26, 13, 126, 126, 126, 22], 
        [78, 78, 78, 6, 8, 56, 126, 126, 126, 126, 126], 
        [78, 78, 78, 78, 9, 9, 126, 126, 126, 126, 126]], 
        [[16, 114, 114, 114, 64, 64, 65, 65, 65, 66, 66], 
        [114, 114, 114, 114, 80, 64, 65, 65, 66, 66, 66], 
        [60, 114, 114, 80, 80, 80, 65, 65, 66, 66, 66], 
        [60, 60, 42, 80, 80, 80, 65, 65, 66, 66, 66], 
        [60, 61, 42, 42, 80, 80, 37, 21, 21, 21, 22], 
        [72, 72, 120, 54, 8, 90, 90, 38, 21, 22, 22], 
        [72, 72, 120, 8, 8, 90, 26, 38, 38, 22, 22], 
        [72, 72, 120, 8, 8, 26, 56, 32, 14, 22, 22], 
        [78, 73, 73, 121, 8, 9, 32, 14, 14, 14, 22], 
        [78, 73, 73, 121, 9, 9, 14, 14, 14, 33, 33], 
        [78, 74, 74, 74, 9, 9, 14, 14, 33, 33, 33]], 
        [[16, 16, 114, 114, 80, 64, 65, 65, 66, 66, 66], 
        [16, 114, 114, 114, 80, 80, 65, 65, 66, 66, 66], 
        [60, 114, 114, 80, 80, 80, 65, 66, 66, 66, 66], 
        [61, 61, 61, 80, 80, 81, 81, 66, 66, 66, 66], 
        [61, 61, 61, 80, 80, 81, 81, 66, 66, 66, 22], 
        [72, 62, 62, 8, 8, 81, 26, 38, 38, 22, 22], 
        [72, 120, 120, 8, 8, 8, 56, 32, 14, 22, 22], 
        [73, 73, 73, 121, 8, 9, 56, 14, 14, 14, 22], 
        [73, 73, 121, 121, 9, 9, 9, 14, 14, 33, 33], 
        [73, 74, 74, 121, 9, 9, 9, 57, 33, 33, 33], 
        [74, 74, 74, 74, 9, 10, 10, 57, 33, 33, 34]], 
        [[17, 17, 17, 114, 80, 80, 65, 66, 66, 66, 66], 
        [17, 17, 114, 80, 80, 81, 65, 66, 66, 66, 66], 
        [61, 61, 61, 80, 80, 81, 81, 66, 66, 66, 66], 
        [61, 61, 62, 80, 81, 81, 81, 66, 66, 66, 66], 
        [62, 62, 62, 62, 81, 81, 81, 82, 66, 66, 22], 
        [62, 62, 62, 62, 81, 81, 82, 82, 82, 22, 22], 
        [73, 73, 121, 121, 8, 9, 56, 14, 14, 14, 22], 
        [73, 73, 121, 121, 9, 9, 9, 14, 14, 33, 33], 
        [73, 74, 121, 121, 9, 9, 9, 57, 33, 33, 33], 
        [74, 74, 74, 122, 9, 10, 10, 57, 33, 33, 34], 
        [74, 74, 74, 122, 122, 10, 10, 10, 33, 58, 34]], 
        [[18, 18, 18, 18, 80, 81, 66, 66, 66, 66, 66], 
        [18, 18, 18, 80, 81, 81, 81, 66, 66, 66, 66], 
        [18, 62, 62, 81, 81, 81, 81, 82, 66, 66, 66], 
        [62, 62, 62, 62, 81, 81, 82, 82, 82, 66, 66], 
        [62, 62, 62, 62, 81, 82, 82, 82, 82, 82, 66], 
        [62, 62, 62, 62, 82, 82, 82, 82, 82, 82, 22], 
        [62, 62, 121, 121, 9, 9, 82, 82, 57, 33, 33], 
        [73, 121, 121, 121, 9, 9, 9, 57, 57, 33, 33], 
        [74, 74, 74, 122, 9, 10, 10, 57, 33, 33, 34], 
        [74, 74, 122, 122, 122, 10, 10, 10, 33, 58, 34], 
        [74, 74, 122, 122, 122, 10, 10, 10, 58, 58, 34]], 
        [[18, 18, 18, 18, 18, 81, 81, 66, 66, 66, 66], 
        [18, 18, 18, 18, 81, 81, 82, 82, 66, 66, 66], 
        [18, 18, 62, 62, 81, 82, 82, 82, 82, 66, 66], 
        [62, 62, 62, 62, 82, 82, 82, 82, 82, 82, 66], 
        [62, 62, 62, 62, 82, 82, 82, 82, 82, 82, 82], 
        [62, 62, 62, 62, 82, 82, 82, 82, 82, 82, 33], 
        [62, 62, 121, 121, 82, 82, 82, 82, 82, 33, 33], 
        [74, 74, 122, 122, 9, 10, 10, 10, 57, 33, 58], 
        [74, 74, 122, 122, 122, 10, 10, 10, 58, 58, 34], 
        [74, 122, 122, 122, 122, 10, 10, 10, 58, 58, 34], 
        [74, 122, 122, 122, 122, 10, 10, 10, 58, 58, 34]]]
    }


estimationlookupdict = {}

def addestimate(n,todict=False):
    '''adds genestimation(n) to estimationlookup or estimationlookupdict at index n'''
    if todict:
        global estimationlookup
        estimationlookup[n] = genestimation(n)
    else:
        global estimationlookupdict
        estimationlookupdict[n] = genestimationdict(n)

def genestimation(n):
    '''returns a nested list by estimating approximate() on interval n in every axis'''
    rl = []
    for rn in range(n+1):
        gl = []
        for gn in range(n+1):
            bl = []
            for bn in range(n+1):
                r = (rn+.5)*255/n
                g = (gn+.5)*255/n
                b = (bn+.5)*255/n
                i = approximate((r,g,b))
                bl.append(i)
            gl.append(bl)
        rl.append(gl)
    return rl


def genestimationdict(n):
    '''returns a dict with indexes (r,g,b) by estimating approximate() on interval n in every axis'''
    lookup = {}
    for rn in range(n+1):
        for gn in range(n+1):
            for bn in range(n+1):
                r = (rn+.5)*255/n
                g = (gn+.5)*255/n
                b = (bn+.5)*255/n
                i = approximate((r,g,b))
                lookup[(rn,gn,bn)] = i
    return lookup


def colordifference(testcolor,comparecolor):
    '''returns rgb distance squared'''
    d = ((testcolor[0]-comparecolor[0])**2+
        (testcolor[1]-comparecolor[1])**2+
        (testcolor[2]-comparecolor[2])**2)
    return d

def approximate(color):
    '''returns best minecraft color code from rgb'''
    try:
        return allcolorsinversemap[color]
    except KeyError:
        color = min(allcolors,key=partial(colordifference,color))
        return allcolorsinversemap[color]

if alphacolor != (0,0,0):
    addestimate(10)