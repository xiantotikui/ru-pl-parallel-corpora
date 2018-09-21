import xmltodict
from os.path import join
from os import walk
from transliterate import translit, get_available_language_codes

source = []
target = []
for (dirpath, dirnames, filenames) in walk('pelcra_par_5'):
    for one in filenames:
        if one == 'text.xlf':
            path = join(dirpath, one)
            with open(path) as fd:
                doc = xmltodict.parse(fd.read())

            for example in doc['xliff']['file']['body']['trans-unit']:
                if example['source'] == None or example['target'] == None:
                    continue
                source.append(example['source'].replace('\n', ' '))
                ru = example['target'].replace('\n', ' ')
                target.append(translit(ru, 'ru', reversed=True))

src_len = len(source)
src_train_len = int(0.9 * src_len)
src_test_val_len = int(0.1 * src_len)
src_train = source[:src_train_len]
src_test_val = source[src_test_val_len:]
src_test = src_test_val[:len(src_test_val)//2]
src_val = src_test_val[len(src_test_val)//2:]

tgt_len = len(target)
tgt_train_len = int(0.9 * tgt_len)
tgt_test_val_len = int(0.1 * tgt_len)
tgt_train = target[:tgt_train_len]
tgt_test_val = target[tgt_test_val_len:]
tgt_test = tgt_test_val[:len(tgt_test_val)//2]
tgt_val = tgt_test_val[len(tgt_test_val)//2:]

outF = open("src_train.txt", "w")
for line in tgt_train:
  if line == None:
    continue
  outF.write(line)
  outF.write("\n")
outF.close()

outF = open("src_test.txt", "w")
for line in tgt_test:
  if line == None:
    continue
  outF.write(line)
  outF.write("\n")
outF.close()

outF = open("src_val.txt", "w")
for line in tgt_val:
  if line == None:
    continue
  outF.write(line)
  outF.write("\n")
outF.close()

outF = open("tgt_train.txt", "w")
for line in src_train:
  if line == None:
    continue
  outF.write(line)
  outF.write("\n")
outF.close()

outF = open("tgt_test.txt", "w")
for line in src_test:
  if line == None:
    continue
  outF.write(line)
  outF.write("\n")
outF.close()

outF = open("tgt_val.txt", "w")
for line in src_val:
  if line == None:
    continue
  outF.write(line)
  outF.write("\n")
outF.close()
