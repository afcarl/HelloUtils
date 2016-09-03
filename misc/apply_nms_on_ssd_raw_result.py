import numpy as np

ssd_detect_file_name = 'ssd_detect_outfile_cls_loc_val_iter470000_conf0.01.txt'
output_detect_file_name = 'ssd_detect_outfile_cls_loc_val_iter470000_nms.txt'

# https://github.com/rbgirshick/fast-rcnn/blob/master/lib/utils/nms.py
def nms(dets, thresh):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    scores = dets[:, 4]

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)
        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0.0, xx2 - xx1 + 1)
        h = np.maximum(0.0, yy2 - yy1 + 1)
        inter = w * h
        ovr = inter / (areas[i] + areas[order[1:]] - inter)

        inds = np.where(ovr <= thresh)[0]
        order = order[inds + 1]

    return keep

def write_file(out_file, dets, image_name):
    for i in xrange(len(dets)):
        x1 = int(dets[i, 0])
        y1 = int(dets[i, 1])
        x2 = int(dets[i, 2])
        y2 = int(dets[i, 3])
        score = dets[i, 4]
        out_file.write('{} {} {} {} {} {}\n'.format(image_name, x1, y1, x2, y2, score))

if __name__ == '__main__':
    ssd_detect_file = open(ssd_detect_file_name, 'r')
    detect_result_items = [line.rstrip('\n') for line in ssd_detect_file]
    ssd_detect_file.close()

    output_detect_file = open(output_detect_file_name, 'w')

    #CONF_THRESH = 0.6
    CONF_THRESH = 0.1
    NMS_THRESH = 0.45

    prev_image_name = ''
    dets = np.zeros((0, 5), dtype=np.float32)
    for idx, item in enumerate(detect_result_items):
        image_path, label_idx, score, x1, y1, x2, y2 = item.split(' ')
        image_name = image_path.split('/')[-1]

        x1 = float(x1)
        y1 = float(y1)
        x2 = float(x2)
        y2 = float(y2)
        score = float(score)

        if score < CONF_THRESH:
            # fix bug: last item
            if idx == len(detect_result_items) - 1:
                print('Run NMS on image: {}'.format(image_name))
                keep = nms(dets, NMS_THRESH)
                dets = dets[keep]
                write_file(output_detect_file, dets, prev_image_name)

            continue

        if idx == 0:
            dets = np.vstack((dets, [x1, y1, x2, y2, score]))
            prev_image_name = image_name
            continue
        else:
            if image_name != prev_image_name or idx == len(detect_result_items) - 1:
                print('Run NMS on image: {}'.format(image_name))
                keep = nms(dets, NMS_THRESH)
                dets = dets[keep]

                write_file(output_detect_file, dets, prev_image_name)

                prev_image_name = image_name

                # re-init
                dets = np.zeros((0, 5), dtype=np.float32)
            dets = np.vstack((dets, [x1, y1, x2, y2, score]))

    output_detect_file.close()
