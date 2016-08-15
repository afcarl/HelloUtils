import os.path as osp
import cv2
import xml.etree.ElementTree as ET

GREEN = (0, 255, 0) # pos
RED = (0, 0, 255) # neg

task = 'val2'
draw_gt_box = False
draw_pred_box = True

det_200_labelmap_file = 'det_200_labelmap.txt'
image_name_list = 'val2.txt'
#image_name_list = 'test.txt'
image_dir = '/path/to/data/ILSVRC/Data/DET/val/'
#image_dir = '/path/to/data/ILSVRC/Data/DET/test/'
annotation_dir = '/path/to/data/ILSVRC/Annotations/DET/val/'
#annotation_dir = '/path/to/data/ILSVRC/Annotations/DET/test/'
out_file = 'eval_outfile_val2.txt'
#out_file = 'eval_outfile_test.txt'
image_with_anno_dir = '/path/to/jinbin.lin/ilsvrc_det_result/val2/'
#image_with_anno_dir = '/path/to/jinbin.lin/ilsvrc_det_result/test/'
saving_dir = '/path/to/jinbin.lin/ilsvrc_det_result/val2_ssd_v5_500000/'
#saving_dir = '/path/to/jinbin.lin/ilsvrc_det_result/test_ssd_v5_500000/'

def parse_xml(filename):
    """ Parse a ILSVRC 2015 DET xml file """
    tree = ET.parse(filename)
    objects = []
    for obj in tree.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(bbox.find('xmin').text),
                                int(bbox.find('ymin').text),
                                int(bbox.find('xmax').text),
                                int(bbox.find('ymax').text)]
        objects.append(obj_struct)

    return objects

def read_det_200_labelmap(filename):
    labelmap_file = open(filename, 'r')
    det_items = [line.rstrip('\n') for line in labelmap_file]
    labelmap_file.close()
    name_to_labelidx = {}
    labelidx_to_name = {}
    for idx, item in enumerate(det_items):
        name, label_idx, display_name = item.split(' ')
        name_to_labelidx[name] = {'label_idx': label_idx, 'display_name': display_name}
        labelidx_to_name[label_idx] = {'name': name, 'display_name': display_name}
    return name_to_labelidx, labelidx_to_name

if __name__ == '__main__':
    det_200_name_to_labelmap, det_200_labelmap_to_name = read_det_200_labelmap(det_200_labelmap_file)

    image_list_file = open(image_name_list, 'r')
    image_items = [line.rstrip('\n') for line in image_list_file]
    image_list_file.close()

    # draw ground-truth bbox
    if draw_gt_box:
        for idx, image_name in enumerate(image_items):
            print('Create ground-truth image {}: {}'.format(idx, image_name))

            #print annotation_dir
            #print image_name

            anno_file_name = osp.join(annotation_dir, image_name + '.xml')
            bbox_object = parse_xml(anno_file_name)

            image_path = osp.join(image_dir, image_name + '.JPEG')
            image = cv2.imread(image_path)
            #print bbox_object

            for b_i in xrange(len(bbox_object)):
                name = bbox_object[b_i]['name']
                #print('  name {}: {}'.format(b_i, name))
                xmin, ymin, xmax, ymax = bbox_object[b_i]['bbox']
                label_idx = int(det_200_name_to_labelmap[name]['label_idx'])
                display_name = det_200_name_to_labelmap[name]['display_name']
                cv2.rectangle(image, (xmin, ymin), (xmax, ymax), GREEN, 1)
                cv2.putText(image, '{}: {}'.format(label_idx, display_name),
                            (xmin, ymin-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, GREEN)
            save_path = osp.join(image_with_anno_dir, image_name + '.JPEG')

            #print save_path

            cv2.imwrite(save_path, image)

            #if len(bbox_object) > 1:
                #print('  bbox_object: {}'.format(len(bbox_object)))
                #break

    if draw_pred_box:
        predict_file = open(out_file, 'r')
        list_items = [line.rstrip('\n') for line in predict_file]
        predict_file.close()

        # draw predicted bbox
        for idx, item in enumerate(list_items):
            image_path, label_idx, score, xmin0, ymin0, xmax0, ymax0 = item.split(' ')
            image_name = image_path.split('/')[-1]

            print('Create predicted bbox image {}: {}'.format(idx, image_name))

            display_name = det_200_labelmap_to_name[str(label_idx)]['display_name']
            xmin = int(xmin0)
            ymin = int(ymin0)
            xmax = int(xmax0)
            ymax = int(ymax0)

            image_with_anno_path = osp.join(image_with_anno_dir, image_name)
            image_saving_path = osp.join(saving_dir, image_name)
            image_to_open = image_with_anno_path
            if osp.isfile(image_saving_path):
                image_to_open = image_saving_path

            #print('image_with_anno: {}'.format(image_with_anno_path))
            #print('image_saving: {}'.format(image_saving_path))
            #print('image_to_open: {}'.format(image_to_open))

            image = cv2.imread(image_to_open)
            cv2.rectangle(image, (xmin, ymin), (xmax, ymax), RED, 1)
            cv2.putText(image, '{}: {}: {:.6f}'.format(label_idx, display_name, float(score)),
                        (xmin, ymin+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, RED)
            cv2.imwrite(image_saving_path, image)

            #if idx > 2:
            #    break
