# Template Matching
# source : https://forum.yazbel.com/t/real-time-template-matching/1076
import cv2

def detect(frame, temp, w, h):

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(frame, temp, cv2.TM_CCORR_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    return (max_val, top_left, bottom_right)

if __name__ == '__main__':
    image = cv2.imread('try.jpg') # aranılan resim
    template = cv2.imread('tr.png', 0) # aranan resim

    tW, tH = template.shape[::-1]
    result = detect(image, template, tW, tH); print(result)

    cv2.rectangle(image, *result[1:], (0, 255, 0), 2)
    cv2.imshow('match', image)

    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()

"""
# Gerçek Zamanlı Template Matching
# templates diye klasör açıp onun içine aranacak şeyleri koy
#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#

__author__ = '@laszlokuehl'

import os
import cv2

class TemplateMatch:
    def __init__(self, templates):
        self.cam = cv2.VideoCapture(0)

        for temp in templates.keys():
            templates[temp] = (templates[temp], *templates[temp].shape[::-1])

        self.templates = templates

    def detect(self, frame, temp, w, h):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        result = cv2.matchTemplate(frame, temp, cv2.TM_CCORR_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        return (max_val, top_left, bottom_right)

    def main(self):
        while True:
            _, image = self.cam.read()

            for name, temp in self.templates.items():
                result = self.detect(image, *temp)

                if result[0] >= 0.98:
                    label = '{}: {:.2f}%'.format(name, result[0] * 100)

                    cv2.putText(image, label, (result[1][0], result[1][1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (32, 32, 32), 1)
                    cv2.rectangle(image, *result[1:], (32, 32, 32), 2)
                else:
                    print('{}: {:.2f}%'.format(name, result[0] * 100))

            cv2.imshow('temp match', image)

            if (cv2.waitKey(5) & 0xFF) == 27:
                break

        cv2.destroyAllWindows()

if __name__ == '__main__':
    app = TemplateMatch(
        dict(
            [(img.split('.')[0], cv2.imread('templates/' + img, 0)) for img in os.listdir('templates') if 'png' in img]
        )
    )
    app.main()
"""
