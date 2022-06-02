# Deal with experiment 1 first
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

result_images = []

experiments = [1,2]
for experiment in experiments:
    for subject in range(1, 109 + 1):
        for segment in range(12):
            images_2 = []
            for channel in range(64):
                print("Subject ", subject, "Channel", channel, " Segment", segment)

                images_2.append([cv2.imread(x, cv2.IMREAD_UNCHANGED) for x in [
                    'F:\\experiment\\experiment'+str(experiment)+'_new_image_output_1-110\\subject_' + str(subject) +
                    '\\channel_' + str(channel) + '\\example_' + str(segment) + '.png']])
                #         1st iteration would be images_2 = [.../channel_0/example_0, .../channel_1/example_0,.../channel_2/example_0,.../channel_3/example_0
                print('F:\\experiment\\experiment'+str(experiment)+'_new_image_output\\subject_' + str(subject) +
                    '\\channel_' + str(channel) + '\\example_' + str(segment) + '.png')
                print("__________")

            for i in images_2:
                print(np.asarray(i).shape)


            imgs_comb = np.vstack((np.asarray(i[0]) for i in images_2))

            imgs_comb = cv2.cvtColor(imgs_comb, cv2.COLOR_RGBA2RGB)
            imgs_comb = cv2.resize(imgs_comb, (256, 256))

            if os.path.isdir('D:\\AI_CW_Merge\\64-Channel\\Experiment_'+str(experiment)+'_stacked_image\\'):
                print("Directory exists")
            else:
                os.mkdir('D:\\AI_CW_Merge\\64-Channel\\Experiment_' + str(experiment) + '_stacked_image\\')
            # Folder to save
            cv2.imwrite('D:\\AI_CW_Merge\\64-Channel\\Experiment_'+str(experiment)+'_stacked_image\\experiment_'+str(experiment)+'_subject_' + str(subject) + '_segment_' + str(segment) + '.png',
                        imgs_comb)
            print("\n Next Segment")

            del (imgs_comb)
