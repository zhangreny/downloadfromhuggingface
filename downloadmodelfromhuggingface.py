from huggingface_hub import snapshot_download

repo_id = "THUDM/chatglm3-6b"
local_dir = "chatglm3-6b-int4/"
local_dir_use_symlinks = False

snapshot_download(repo_id=repo_id, local_dir=local_dir, local_dir_use_symlinks=local_dir_use_symlinks)


