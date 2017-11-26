import view_tkinter_screens as view
import inter_screens        as face
import script_screens       as do
import data                 as data
import keep_bin             as keep

for module in [view, face, do, data, keep]:
    module.view = view;    module.face = face;    module.do = do
    module.data = data;    module.keep = keep

#view.view = do.view = data.view = keep.view = view
#view.do   = do.do   = data.do   = keep.do   = do
#view.data = do.data = data.data = keep.data = data
#view.keep = do.keep = data.keep = keep.keep = keep

do.main()