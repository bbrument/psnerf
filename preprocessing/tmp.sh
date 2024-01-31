CUDA_VISIBLE_DEVICES=0 \
python test.py \
    --retrain data/models/LCNet_CVPR2019.pth.tar \
    --retrain_s2 data/models/NENet_CVPR2019.pth.tar \
    --benchmark UPS_Custom_Dataset \
    --bm_dir ../dataset/buddha