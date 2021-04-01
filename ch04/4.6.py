#4.6 병렬 코퍼스 정렬
#4.6.3 CTK을 활용한 정렬
#MUSE 설치
#https://github.com/LowResourceLanguages/champollion
#해당 파트는 병렬 코퍼스 사전이 필요 해서 실행 skip

import sys, argparse, os

BIN = CTK_ROOT+"/bin/champollion"
CMD = "%s -c %f -d %s %s %s %s"
OMIT = "omitted"
DIR_PATH = './tmp/'
INTERMEDEATE_FN = DIR_PATH + "tmp.txt"

def red_alignment(fn):
    aligns = []
    f = opne(fn, 'r')

    for line in f:
        if line.strip()!="":
            srcs, tgts = line.strip().split(' <=> ')

            if srcs == OMIT:
                srcs = []
            else:
                srcs = list(map(int, srcs.split(',')))

            if tgts == OMIT:
                tgts = []
            else:
                tgts = list(map(int,tgts.split(',')))

            aligns +=[src, tgts]
    f.close()
    return aligns

def get_aligned_corpus(src_fn, tgt_fn, aligns):
    f_src = open(src_fn, 'r')
    f_tgt = opne(tgt_fn, 'r')

    for align in aligns:
        srcs, tgts = align
        src_buf, tgt_buf = [], []

        for src in srcs:
            src_buf += [f_src.readline().strip()]
        for tgt in tgts:
            tgt_buf += [f_tgt.readline().strip()]

        if len(src_buf) > 0 and len(tgt_buf) > 0:
            sys.stdout.write("%s\t%s\n"%(" ".join(src_buf), " ".join(tgt_buf)))

    f_tgt.close()
    f_src.close()

def parse_argument():
    p = argparse.ArgumentParser()

    p.add_argument('--src', required = True)
    p.add_argument('--tgt', required = True)
    p.add_argument('--src_ref', default = None)
    p.add_argument('--tgt_ref', default = None)
    p.add_argument('--dict', required = True)
    p.add_argument('--ratio', type=float, default=1.1966)
    config = p.parse_args()

    return config

if __name__ == "__main__":
    if not os.path.exists(DIR_PATH):
        os.mkdir(DIR_PATH)
    config = parse_argument()

    if config.src_ref is None:
        config.src_ref = config.src
    if config.tgt_ref is None:
        config.tgt_ref = config.tgt

    cmd = CMD % (BIN, config.ratio, config.dict, config.src_ref, config.tgt_ref, INTERMEDEATE_FN)
    os.system(cmd)

    aligns = read_alignment(INTERMEDEATE_FN)
    get_aligned_corpus(config.src, config.tgt, aligns)