import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
    def test_dataset(self):
        assertGreater()

    def ppt_work(self, save_dir):
        prs = Presentation()
        dir_list = os.listdir(target)  # 읽어오고자 하는 폴더위치 삽입
        print(dir_list)

        blank_slide_layout = prs.slide_layouts[6]  # 이미지를 넣을 슬라이드 생성
        title_slide_layout = prs.slide_layouts[0]  # 텍스트를 넣을 슬라이드 생성
        text_slide = prs.slides.add_slide(title_slide_layout)
        text_slide.shapes.title.text = target.split("\\")[-1]

        for slidetitle in dir_list:  # case의 숫자만큼 반복
            dir_path = target + '/' + slidetitle
            img_list = os.listdir(dir_path)  # 이미지 파일 불러오기
            text_slide = prs.slides.add_slide(title_slide_layout)
            text_slide.shapes.title.text = slidetitle  # case 번호를 보여주는 슬라이드

            for image in tqdm(img_list):  # 이미지 설정

                left = Inches(1)
                width = Inches(7.5)
                height = Inches(7.5)
                top = Inches(0)

                image_slide = prs.slides.add_slide(blank_slide_layout)
                img_path = dir_path + '/' + image
                pic = image_slide.shapes.add_picture(img_path, left, top, width=width, height=height)

        direction = save_dir + '/' + 'DataSet.pptx'
        prs.save(direction)


if __name__ == '__main__':
    unittest.main()

