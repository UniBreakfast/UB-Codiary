import view_console_screens as view
import inter_screens        as face
import script_screens       as do
import data                 as data
import keep_bin             as keep

for module in [view, face, do, data, keep]:
    module.view = view;    module.face = face;    module.do = do
    module.data = data;    module.keep = keep


do.main()