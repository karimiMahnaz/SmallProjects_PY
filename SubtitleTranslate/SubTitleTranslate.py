from translate import Translator
import os

translator = Translator(to_lang='fa')

text = 'I love programming.'
print(translator.translate(text))

filepath = "/Users/taktakro/Desktop/SmallProjects_PY/SubtitleTranslate"
filename1 = "S01E10.720p.WEB_.H264-GGEZ-No-HI.srt"
filename2 = "S01E10.720p.WEB_.H264-GGEZ-No-HI.txt"

nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']



with open(os.path.join(filepath, filename1), "+r") as f:
    sub_lines = f.readlines()

with open(os.path.join(filepath, filename2), 'w', encoding="utf-8") as f:
    for line_en in sub_lines:
        #print(line_en)
        if line_en[0] in nums:
            f.write(line_en)

        elif line_en=='/n':
            f.write('/n')
        else:
            if line_en:
                print(line_en)
                line_fa = translator.translate(line_en)
                f.write(line_fa)

