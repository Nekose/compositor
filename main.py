from src.merge import two_way_merge, four_way_merge, three_way_merge
import os
source1 = "src/images/Case_1019/complaint"
source1label = ""
source2 = "src/images/Case_1019/jackson"
source2label = ""
destination = "top_row"

#four_way_merge("src/images/one","one","src/images/two","two","src/images/three","three","src/images/four","four","Final")
three_way_merge("src/images/one","Position One - Neg Control","src/images/two","Position two - Neg Control","src/images/three","Position Three - SSA Control","Final")

#four-way-merge
# source1,label1 = ("1x","1x 30ul wash")
# source2,label2 = ("20x","20x 30ul washes")
# source3,label3 = ("Heavy","5x 100ul washes")
# source4,label4 = ("Control","Control - 5x 30ul washes")
#
# print("first merge")
# two_way_merge("src/images/" + source1, label1, "src/images/" + source2, label2, source1 + source2)
# print("second merge")
# two_way_merge("src/images/" + source3, label3, "src/images/" + source4, label4, source3 + source4)
# print("Final merge")
# two_way_merge("src/images/" + source1 + source2, "", "src/images/" + source3 + source4, "", "Final", horizontal=False)