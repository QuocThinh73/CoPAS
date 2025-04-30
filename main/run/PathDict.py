# ----------------------------------
# This file is used to define the path of the data and the cache file


# Thư mục gốc chứa data
dataroot        = "/content/CoPAS"

# Định nghĩa các dataset cấu hình tại đây
dataset_dict = {
    "Internal": {
        "train_label"  : dataroot + "/samplelabels.csv",
        "train_path"   : dataroot + "/SampleData",
        "val_label"    : dataroot + "/samplelabels.csv",
        "val_path"     : dataroot + "/SampleData",
        "test_label"   : dataroot + "/samplelabels.csv",
        "test_path"    : dataroot + "/SampleData",
        "cache_path"   : dataroot + "/cache",
        "center_file"  : "",
        "doctor_file"  : "",
        "modal"        : [
            "sag PDW",
            "sag T2WI",
            "cor PDW",
            "axi PDW",
            "cor T1WI"
        ]
    }
}

# Thư mục chứa script chạy
CodePath        = "/content/CoPAS/main/run"

# Thư mục lưu kết quả đánh giá của bác sĩ (nếu có)
DocEvlPath      = "/content/CoPAS/doctor_eval"

# Thư mục lưu experiment (logs, checkpoints,…)
ExpFolder       = "/content/CoPAS/experiments"

# Thư mục chứa pretrained weights (nếu dùng)
pretrain_folder = "/content/CoPAS/pretrained"
