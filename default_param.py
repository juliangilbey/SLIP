{
# Image
'N_X' : 256, # size of images
'N_Y' : 256, # size of images
'do_mask'  : False, # used forinstance in the Matching Pursuit algorithm self.pe.do_mask
'figpath' : 'figures/',
'matpath' : 'mat/',
'datapath' : '../AssoField/database/',
'ext' : '.pdf',
'seed': None, # a seed for the Random Number Generator (RNG) for picking images in databases, set to None or a given number to freeze the RNG
'N_image': None, # number of images to pick in a database, set to None if you want to pick all in the database
# whitening parameters:
'white_name_database' : 'serre07_distractors',
'white_n_learning' : 400,
'white_N' : .07,
'white_N_0' : .0, # olshausen = 0.
'white_f_0' : .4, # olshausen = 0.2
'white_alpha' : 1.4,
'white_steepness' : 4.,
'white_recompute' : False,
'white_learn' : False,
}
