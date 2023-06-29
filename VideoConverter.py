import os
from pathlib import Path
import moviepy.editor as moviepy

path = r""
destine=r""
int_ext='.mkv'
out_ext='.mp4'

for (root, dirs, files) in os.walk(path):
    for f in files:
        f=Path(f)
        if f.suffix==int_ext:
            int_dir=Path(root).joinpath(f)
            out_dir=Path(destine).joinpath(f.with_suffix(out_ext))
            if out_dir.exists()==False:
                convert = moviepy.VideoFileClip(str(int_dir))
                convert.write_videofile(str(out_dir))
                convert.close()