from multiprocessing import freeze_support
freeze_support()

print("initiating")
import sys
a = ["--gpu", "0", "--epoch", "100", "--batch_size", "1", "--lr", "5e-5"]
# a.extend(["--debug"])
sys.argv.extend(a)



import os
import torch

from run.Args import args
from run.train import run
from model.model import Multi_view_Knee
from data.dataloader import test_ds_dict
from val_with_save import val_with_save

import pandas as pd
from torch.utils.data import DataLoader, Subset

def main():
    print("running")
    if args.test:
        assert args.weight_path != "", "Please specify the weight path"
        args.active_branch = [1,1,1]
        model = Multi_view_Knee()
        model_file = args.weight_path
        # model.load_state_dict(torch.load(model_file), strict=False)
        # state_dict = torch.load(model_file, map_location=torch.device('cpu'))
        state_dict = torch.load(model_file, map_location='cpu')
        model.load_state_dict(state_dict, strict=False)
        model = model.cpu().float()
        test_dataset = test_ds_dict['Internal']
        test_dataset = Subset(test_dataset, list(range(5)))
        # show_CAM(net=model, dataset=test_dataset)
        test_loader = DataLoader(
            test_dataset,
            batch_size=1,
            shuffle=False,
            num_workers=3,
            pin_memory=False
        )
        model.eval()
        records = []
        with torch.no_grad():
            for images, _, ids in test_loader:
                # forward
                final_pred, *_ = model(images)           # shape (1,12)
                probs = torch.sigmoid(final_pred)[0]     # shape (12,)
                probs = probs.cpu().numpy()

                rec = {'id': ids[0]}
                # Chỉ lưu xác suất
                for i, p in enumerate(probs):
                    rec[f'prob_{i}'] = float(p)
                records.append(rec)

        # Xuất CSV
        df = pd.DataFrame(records)
        out_dir = args.log_folder
        os.makedirs(out_dir, exist_ok=True)
        csv_path = os.path.join(out_dir, 'test_predictions.csv')
        df.to_csv(csv_path, index=False)
        print(f"Saved probabilities to: {csv_path}")
        # val_with_save(model, test_dataset)
    else:
        run()
        
        
if __name__ == "__main__":
    main()