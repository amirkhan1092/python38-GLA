ele = [[2, 3, [4, [[[[[4]]]]]]], [2, 4, 6], [3, 2], [] , 4, 6]

flatten = []
while 1:
    for c, k in enumerate(ele):
        if type(k) is tuple or type(k) is list:
            flatten.extend(k)
        else:
            flatten.append(k)
        print(f'step {c}',flatten)
    ele = flatten[:]
    flatten.clear()
    if list not in [type(i) for i in ele]:
        break


print(ele)
# sns.scatterplot(
#     x='mean area',
#     y='mean compactness',
#     hue='benign',
#     data=X_test.join(y_test, how='outer')
# )