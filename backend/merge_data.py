import pandas as pd
import glob
import os

# ✅ === CONFIG ===
# Absolute path to your .dat files
DATA_PATH = "/Users/almarai/Private Projects/Pacify/Pacify/data/Protocol"

# ✅ === COLUMN NAMES ===
# Based on PAMAP2 dataset description
columns = ['timestamp', 'activityID', 'heart_rate']

# Add IMU hand columns
imu_hand = [f'hand_col_{i}' for i in range(1, 18)]  # 4-20 inclusive

# Add IMU chest columns
imu_chest = [f'chest_col_{i}' for i in range(1, 18)]  # 21-37 inclusive

# Add IMU ankle columns
imu_ankle = [f'ankle_col_{i}' for i in range(1, 18)]  # 38-54 inclusive

columns += imu_hand + imu_chest + imu_ankle

print(f"Total columns: {len(columns)}")  # Should be 54

# ✅ === Load and merge ===
all_files = glob.glob(os.path.join(DATA_PATH, "*.dat"))

dfs = []

for file in all_files:
    print(f"Loading {file} ...")
    df = pd.read_csv(
        file,
        sep=' ',
        header=None,
        names=columns,
        engine='python'
    )

    # Optional: Add subject ID for traceability
    subject_id = os.path.basename(file).split('.')[0]
    df['subjectID'] = subject_id

    dfs.append(df)

merged_df = pd.concat(dfs, ignore_index=True)

print(f"✅ Merged {len(all_files)} files. Final shape: {merged_df.shape}")

# ✅ === Save to CSV ===
output_csv = os.path.join(DATA_PATH, "PAMAP2_MERGED.csv")
merged_df.to_csv(output_csv, index=False)
print(f"✅ Saved merged CSV to: {output_csv}")
