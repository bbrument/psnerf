# scenes="bear buddha cow pot2 reading"
# scenes="buddha"

# for scene in $scenes; do
#     mkdir -p "dataset/${scene}/sdm_out"
#     cp dataset/${scene}/sdps_out_l96/light_*_pred.npy "dataset/${scene}/sdm_out"
#     mv "dataset/DiLiGenT-MV_crop/${scene}PNG/img" "dataset/${scene}/sdm_out/outimg"
#     mv "dataset/DiLiGenT-MV_crop/${scene}PNG/npy" "dataset/${scene}/sdm_out/outnpy"
# done

# GPU_ID=0

# # python light_avg.py --obj buddha --path dataset --light_intnorm --sdm
# cd stage1
# # python train.py configs/buddha.yaml --gpu $GPU_ID
# # python extract_mesh.py --obj_name buddha
# python shape_extract.py --gpu $GPU_ID --obj_name buddha --expname test_1 --load_iter 100000 --visibility
# cd ../stage2
# python train.py --conf confs/buddha.conf --gpu $GPU_ID
# python eval.py --gpu $GPU_ID --obj_name buddha --expname test_1
# cd ..
# python evaluation.py --obj buddha --expname test_1 --test_out_dir ./stage2/test_out

GPU_ID=0
OBJ_NAME="buddha"

# cd preprocessing
# CUDA_VISIBLE_DEVICES=$GPU_ID python test.py \
#     --retrain data/models/LCNet_CVPR2019.pth.tar \
#     --retrain_s2 data/models/NENet_CVPR2019.pth.tar \
#     --benchmark UPS_Custom_Dataset \
#     --bm_dir ../dataset/$OBJ_NAME

# cd ..
# python light_avg.py \
#     --obj $OBJ_NAME \
#     --path dataset \
#     --light_intnorm \
#     --sdps

cd stage1
python train.py \
    ../data/stage1/$OBJ_NAME/test_1/config.yaml
    --gpu $GPU_ID
# python shape_extract.py \
#     --gpu $GPU_ID \
#     --obj_name $OBJ_NAME \
#     --expname test_sdps \
#     --load_iter 100000 \
#     --visibility

# cd ../stage2
# python train.py xxxx
# # python eval.py xxxx

# cd ..