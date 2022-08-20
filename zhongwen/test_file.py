import unittest

class Test(unittest.TestCase):
    def test_file_location(self):
        from file import FileLocation
        line = r'File "d:\github\zhongwen\test_file.py", line 9, in test_file_location'

        f = FileLocation(line)
        self.assertEqual(f.路徑, r'd:\github\zhongwen\test_file.py')
        self.assertEqual(f.列, 9)
 
        line = 'at Object.toBe (jandas.test.js:7:18)'
        f = FileLocation(line)
        self.assertEqual(f.路徑, 'jandas.test.js')
        self.assertEqual(f.列, 7)
        self.assertEqual(f.行, 18)
        
    def test_file(self):
        # from zhongwen.file import 抓取, cache
        # cache.clear()
        # url = 'https://glrs.hl.gov.tw'
        # page = 抓取(url)
        # print(page.find_elements_by_css_selector('table'))
        # self.assertEqual(page[:5], "<html")
        pass

if __name__ == '__main__':
    unittest.main()

