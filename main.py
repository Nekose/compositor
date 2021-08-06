from src.merge import two_way_merge, four_way_merge, three_way_merge
import os
# source1 = "src/images/Case_1019/complaint"
# source1label = ""
# source2 = "src/images/Case_1019/jackson"
# source2label = ""
# destination = "top_row"

#four_way_merge("src/images/one","EtOH lot 2000700","src/images/two","EtOH lot 2106300","src/images/three","EtOH lot 2031000","src/images/four","Control IC Lot","Final")
#three_way_merge("src/images/one","EtOH lot 2000700","src/images/three","EtOH lot 2031000","src/images/four","Control IC Lot","Final")

#four-way-merge
source1,label1 = ("one","Previous 1/22/21")
source2,label2 = ("two","Current 8/4/21")
# source3,label3 = ("Heavy","5x 100ul washes")
# source4,label4 = ("Control","Control - 5x 30ul washes")
#
# print("first merge")
# two_way_merge("src/images/" + source1, label1, "src/images/" + source2, label2, source1 + source2)
# print("second merge")
# two_way_merge("src/images/" + source3, label3, "src/images/" + source4, label4, source3 + source4)
# print("Final merge")
two_way_merge("src/images/" + source1,label1, "src/images/" + source2, label2, "Final", horizontal=True)