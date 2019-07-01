# Path in ZigZag Labelled Binary Tree
# Easy
import math
class Solution:
    def pathInZigZagTree(self, label):
        if label == 0:
            raise Exception("Invalid Input")

        labels = self.get_labels(label)
        #print(labels)
        paths = []
        index = len(labels) - 1
        while index >= 0:
            #print(index)
            paths.insert(0, labels[index])
            index = math.floor((index-1) / 2)
        return paths

    def get_labels(self, label):
        labels = [1]
        count = 1
        layer = 0
        layer_count = 1
        new_label = 1
        while not new_label == label:
            if layer_count >= pow(2, layer):
                if layer % 2 == 0:
                    new_label = labels[count - 1] + pow(2, layer + 1)
                else:
                    new_label = labels[count - 1] + pow(2, layer)
                layer += 1
                layer_count = 1
            else:
                if layer % 2 == 0:
                    new_label = labels[count - 1] + 1
                else:
                    new_label = labels[count - 1] - 1
                layer_count += 1
            labels.append(new_label)
            count += 1
        return labels