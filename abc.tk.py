#!/usr/bin/env python

# This is my Python Version my ABC perl script.

# GitHub Description : Tool to replace command some basic command line functions. This version in Python.

# https://github.com/HuskyCougar/abc.tk.py
# https://github.com/HuskyCougar/abc.tk.py.git
# git clone https://github.com/HuskyCougar/abc.tk.py.git
# https://github.com/HuskyCougar/abc.tk.py/blob/master/abc.tk.py



########################################################################
##                              Updates                               ##
########################################################################

#region    ## Updates ##################################################

# 2024-10-14 11:35:14 # abc__tops__add_replace. Replacing with \n resulted in \n in log. Log now shows "\n"
# 2024-10-14 01:04:34 # abc__tops__split_string_by. Added text tokenizer. This should help with finding good strings to match on when looking for artifacts in text files.
# 2024-10-13 19:13:49 #_sort_lines  Replaced with a new one that adds case-insensitive sorting. Also added domain name, IP address, and email address sorting. 

#endregion ## Updates ##################################################


########################################################################
##                              Imports                               ##
########################################################################

# region     # Imports #################################################

import random
import datetime
import re
import os
import hashlib


from collections import Counter
from inspect import currentframe, getframeinfo

# endregion  # Imports #################################################



########################################################################
#                            Main Function                             #
########################################################################

# region     # Main Function ###########################################

from tkinter import Menu, Tk, Button, Frame, LabelFrame, PanedWindow, Toplevel, Label, Entry
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import font
from tkinter import messagebox
from tkinter import BooleanVar, StringVar

abc = {} # holds TK Mainwindow components
box = {} # Holds data from each box

gopts = {  # set defaults. Will change with GUI later
      "trim_leading_spaces"  : False
    , "trim_trailing_spaces" : True
    , "trim_blank_lines"     : False
    , "read_in_boxes_upper"  : False
    , "read_in_boxes_lower"  : False
    , "read_in_boxes_dedupe" : False
    , "record_separator"     : "\n"
    , "column_separator"     : ","
}


def main() :  ## 914751229efdd8016424481f8f8342be # 2024-10-14 17:13:17 #

    build_main_window()
    menubar_file()
    menubar_abc()
    menubar_compare()
    menubar_convert()
    menubar_tops()
    menubar_fops()
    menubar_code()
    menubar_misc()
    menubar_options()

    abc[  "main_window" ].mainloop()


abc_window_title = "ABC : 2024-10-14"
print( f'# INFO # {datetime.datetime.now():%Y-%m-%d %H:%M:%S} # Line : {getframeinfo(currentframe()).lineno:4,d} # Script Name : {getframeinfo(currentframe()).filename}' )
print( f'# INFO # {datetime.datetime.now():%Y-%m-%d %H:%M:%S} # Line : {getframeinfo(currentframe()).lineno:4,d} # Script Version : {abc_window_title}' )

# endregion  # Main Function ###########################################



####################################################################
##                        Build GUI Window                        ##
####################################################################

# region     ## Build GUI Window ###################################

def build_main_window() :  ## f56fc16f56f5fa8e91fd2cd888c45189 # 2024-10-14 17:21:00 #

    abc[  "main_window" ] = Tk()

    abc[  "main_window" ].title( abc_window_title )

    abc[  "main_window" ].option_add('*Dialog.msg.font', 'TkFixedFont')

    abc[  "Adjuster_LR" ] = PanedWindow( abc[  "main_window" ] , orient="horizontal" )

    abc[  "frame_L" ] = Frame( abc[  "main_window" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "frame_L" ].pack( side = "left" , fill = "both" , expand = True )
    abc[  "frame_R" ] = Frame( abc[  "main_window" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "frame_R" ].pack( side = "left" , fill = "both" , expand = True )

    abc[  "Adjuster_LR" ].add( abc[  "frame_L" ] )
    abc[  "Adjuster_LR" ].add( abc[  "frame_R" ] )
    abc[  "Adjuster_LR" ].pack( fill = "both" , expand = True )

    abc[  "Adjuster_AB" ] = PanedWindow( abc[  "frame_L" ] , orient = "vertical" )

    abc[  "frame_A" ] = Frame( abc[  "frame_L" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "frame_A" ].pack( side = "top" , fill = "both" , expand = "yes" )
    abc[  "frame_B" ] = Frame( abc[  "frame_L" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "frame_B" ].pack( side = "top" , fill = "both" , expand = "yes" )

    abc[  "Adjuster_AB" ].add( abc[  "frame_A" ] )
    abc[  "Adjuster_AB" ].add( abc[  "frame_B" ] )
    abc[  "Adjuster_AB" ].pack( fill = "both" , expand = True )

    abc[  "frame_C" ] = Frame( abc[  "frame_R" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "frame_C" ].pack( side = "top" , fill = "both" , expand = "yes" )

    abc[  "LabFrame_A" ] = LabelFrame( abc[  "frame_A" ] , text = "Box A" ) ; abc[  "LabFrame_A" ].pack( side = "top" , fill = "both" , expand = "yes" )
    abc[  "LabFrame_B" ] = LabelFrame( abc[  "frame_B" ] , text = "Box B" ) ; abc[  "LabFrame_B" ].pack( side = "top" , fill = "both" , expand = "yes" )
    abc[  "LabFrame_C" ] = LabelFrame( abc[  "frame_C" ] , text = "Box C" ) ; abc[  "LabFrame_C" ].pack( side = "top" , fill = "both" , expand = "yes" )

    abc[  "LabFrame_A_Top" ] = Frame( abc[  "LabFrame_A" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "LabFrame_A_Top" ].pack( side = "top" ,                expand = "no"  )
    abc[  "LabFrame_A_Bot" ] = Frame( abc[  "LabFrame_A" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "LabFrame_A_Bot" ].pack( side = "top" , fill = "both", expand = "yes" )

    abc[  "LabFrame_B_Top" ] = Frame( abc[  "LabFrame_B" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "LabFrame_B_Top" ].pack( side = "top" ,                expand = "no"  )
    abc[  "LabFrame_B_Bot" ] = Frame( abc[  "LabFrame_B" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "LabFrame_B_Bot" ].pack( side = "top" , fill = "both", expand = "yes" )

    abc[  "LabFrame_C_Top" ] = Frame( abc[  "LabFrame_C" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "LabFrame_C_Top" ].pack( side = "top" ,                expand = "no"  )
    abc[  "LabFrame_C_Bot" ] = Frame( abc[  "LabFrame_C" ] , relief = 'groove' , borderwidth = 1 ) ; abc[  "LabFrame_C_Bot" ].pack( side = "top" , fill = "both", expand = "yes" )

    box[ "A" ] = ScrolledText( abc[  "LabFrame_A_Bot" ] , height = 15 , width = 60 , wrap = "none")
    box[ "B" ] = ScrolledText( abc[  "LabFrame_B_Bot" ] , height = 15 , width = 60 , wrap = "none")
    box[ "C" ] = ScrolledText( abc[  "LabFrame_C_Bot" ] , height = 15 , width = 60 , wrap = "none")

    abc[  "Button_A1" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'A  > B' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[  "Button_A2" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'A >> B' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[  "Button_A3" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'A <> B' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[  "Button_A4" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'A  > C' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[  "Button_A5" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'A >> C' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[  "Button_A6" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'A <> C' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[  "Button_A7" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'Dedupe' , command=lambda: _deduplicate_lines(    **{ "fm_box" : "A"                  } ) ).pack( side = "left" )
    abc[  "Button_A9" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'Sort'   , command=lambda: _sort_lines(           **{ "fm_box" : "A" , "sort_what" : "lines" , "sort_order" : "AZ" , "sort_case" : 0 } ) ).pack( side = "left" )
    abc[  "Button_A8" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'Trim'   , command=lambda: _trim_blank_lines(     **{ "fm_box" : "A"                  } ) ).pack( side = "left" )
    abc[  "Button_AC" ] = Button( abc[  "LabFrame_A_Top" ] , text = 'Clear'  , command=lambda: _clear_box(                           "A"                    ) ).pack( side = "left" )

    abc[  "Button_B1" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'B  > A' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[  "Button_B2" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'B >> A' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[  "Button_B3" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'B <> A' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[  "Button_B4" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'B  > C' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[  "Button_B5" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'B >> C' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[  "Button_B6" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'B <> C' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[  "Button_B7" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'Dedupe' , command=lambda: _deduplicate_lines(    **{ "fm_box" : "B"                  } ) ).pack( side = "left" )
    abc[  "Button_B9" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'Sort'   , command=lambda: _sort_lines(           **{ "fm_box" : "B" , "sort_what" : "lines" , "sort_order" : "AZ" , "sort_case" : 0 } ) ).pack( side = "left" )
    abc[  "Button_B8" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'Trim'   , command=lambda: _trim_blank_lines(     **{ "fm_box" : "B"                  } ) ).pack( side = "left" )
    abc[  "Button_BC" ] = Button( abc[  "LabFrame_B_Top" ] , text = 'Clear'  , command=lambda: _clear_box(                           "B"                    ) ).pack( side = "left" )

    abc[  "Button_C1" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'C  > A' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[  "Button_C2" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'C >> A' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[  "Button_C3" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'C <> A' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[  "Button_C4" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'C  > B' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[  "Button_C5" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'C >> B' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[  "Button_C6" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'C <> B' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[  "Button_C7" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'Dedupe' , command=lambda: _deduplicate_lines(    **{ "fm_box" : "C"                  } ) ).pack( side = "left" )
    abc[  "Button_C9" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'Sort'   , command=lambda: _sort_lines(           **{ "fm_box" : "C" , "sort_what" : "lines" , "sort_order" : "AZ" , "sort_case" : 0 } ) ).pack( side = "left" )
    abc[  "Button_C8" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'Trim'   , command=lambda: _trim_blank_lines(     **{ "fm_box" : "C"                  } ) ).pack( side = "left" )
    abc[  "Button_CC" ] = Button( abc[  "LabFrame_C_Top" ] , text = 'Clear'  , command=lambda: _clear_box(                           "C"                    ) ).pack( side = "left" )

    box[ "A" ].pack( fill = "both" , expand = True )
    box[ "B" ].pack( fill = "both" , expand = True )
    box[ "C" ].pack( fill = "both" , expand = True )


# endregion  ## Build GUI Window ###################################





###############################################################################################################


###############################################################################################################
#                                                                                                             #
#                           #     # ####### #       ######  ####### ######   #####                            #
#                           #     # #       #       #     # #       #     # #     #                           #
#                           #     # #       #       #     # #       #     # #                                 #
#                           ####### #####   #       ######  #####   ######   #####                            #
#                           #     # #       #       #       #       #   #         #                           #
#                           #     # #       #       #       #       #    #  #     #                           #
#                           #     # ####### ####### #       ####### #     #  #####                            #
#                                                                                                             #
###############################################################################################################


###############################################################################################################



########################################################################
##                        ABC Window Functions                        ##
########################################################################

# region     # ABC Window Functions ####################################

def _not_done_yet() :
    print( '# This function not completed yet' )
    messagebox.showinfo( '_not_done_yet' , 'This function is not done yet.' )


def _get_from_box( **kwargs ) :

    timenow = datetime.datetime.now()

    lopts = {}

    try     : lopts[ "trim_leading_spaces"  ] = kwargs[ "trim_leading_spaces"  ] # unless ( defined $lopts{trim_leading_spaces  } ) { $lopts{trim_leading_spaces  } = $main::gopts{trim_leading_spaces  } ; }
    except  : lopts[ "trim_leading_spaces"  ] = gopts[  "trim_leading_spaces"  ]

    try     : lopts[ "trim_trailing_spaces" ] = kwargs[ "trim_trailing_spaces" ] # unless ( defined $lopts{trim_trailing_spaces } ) { $lopts{trim_trailing_spaces } = $main::gopts{trim_trailing_spaces } ; }
    except  : lopts[ "trim_trailing_spaces" ] = gopts[  "trim_trailing_spaces" ]

    try     : lopts[ "trim_blank_lines"     ] = kwargs[ "trim_blank_lines"     ] # unless ( defined $lopts{trim_blank_lines     } ) { $lopts{trim_blank_lines     } = $main::gopts{trim_blank_lines     } ; }
    except  : lopts[ "trim_blank_lines"     ] = gopts[  "trim_blank_lines"     ]

    try     : lopts[ "read_in_boxes_upper"  ] = kwargs[ "read_in_boxes_upper"  ] # unless ( defined $lopts{read_in_boxes_upper  } ) { $lopts{read_in_boxes_upper  } = $main::gopts{read_in_boxes_upper  } ; }
    except  : lopts[ "read_in_boxes_upper"  ] = gopts[  "read_in_boxes_upper"  ]

    try     : lopts[ "read_in_boxes_lower"  ] = kwargs[ "read_in_boxes_lower"  ] # unless ( defined $lopts{read_in_boxes_lower  } ) { $lopts{read_in_boxes_lower  } = $main::gopts{read_in_boxes_lower  } ; }
    except  : lopts[ "read_in_boxes_lower"  ] = gopts[  "read_in_boxes_lower"  ]

    try     : lopts[ "read_in_boxes_dedupe" ] = kwargs[ "read_in_boxes_dedupe" ] # unless ( defined $lopts{read_in_boxes_dedupe } ) { $lopts{read_in_boxes_dedupe } = $main::gopts{read_in_boxes_dedupe } ; }
    except  : lopts[ "read_in_boxes_dedupe" ] = gopts[  "read_in_boxes_dedupe" ]

    try     : lopts[ "record_separator"     ] = kwargs[ "record_separator"     ] # unless ( defined $lopts{record_separator     } ) { $lopts{record_separator     } = $main::gopts{record_separator     } ; }
    except  : lopts[ "record_separator"     ] = gopts[  "record_separator"     ]

    fm_box = kwargs[ "fm_box" ]
    fm_str = box[ fm_box ].get( "1.0" , 'end-1c' )

    #to_val = # todo: figure out what how the user wants the data
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _get_from_box : figure out what how the user wants the data' )

    if lopts[ "record_separator" ] == "singlespace" : fm_lst = _data.splitlines()
    if lopts[ "record_separator" ] == "doublespace" : print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _get_from_box : Not Done Yet' )
    if lopts[ "record_separator" ] == "whitespace"  : fm_lst = fm_str.split( " " )

    if lopts[ "trim_leading_spaces"  ] : fm_lst = [ x.lstrip(" ") for x in fm_lst ]
    if lopts[ "trim_trailing_spaces" ] : fm_lst = [ x.rstrip(" ") for x in fm_lst ]
    if lopts[ "trim_blank_lines"     ] : fm_lst = [ x for x in _data if x.strip() ]

    #todo use this

    # return xxxxxx #


def _clear_box( _box ) :  ## 9bb8bc280d8d407fb3cf6628378d6825 # 2024-04-02 09:30:39 #

    timenow = datetime.datetime.now()
    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _clear_box( {{ "fm_box" : "{_box}" }} )' )

    box[ _box ].delete( "1.0" , "end" )


def _clear_boxes( ) :  ## d5353e966a141af7f93fd41f1af5109a # 2024-04-02 09:30:59 #

    timenow = datetime.datetime.now()
    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _clear_boxes( )' )

    box[ "A" ].delete( "1.0" , "end" )
    box[ "B" ].delete( "1.0" , "end" )
    box[ "C" ].delete( "1.0" , "end" )


def _Apnd_from_File( to_box ) : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _Apnd_from_File : Not Done Yet' )
    messagebox.showinfo( '_Apnd_from_File' , 'This function is not done yet.' )


def _Open_from_Clip( to_box ) : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _Open_from_Clip : Not Done Yet' )
    messagebox.showinfo( '_Open_from_Clip' , 'This function is not done yet.' )


def _Apnd_from_Clip( to_box ) : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _Apnd_from_Clip : Not Done Yet' )
    messagebox.showinfo( '_Apnd_from_Clip' , 'This function is not done yet.' )


def _Save_to_File(   fm_box ) : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _Save_to_File : Not Done Yet' )
    messagebox.showinfo( '_Save_to_File' , 'This function is not done yet.' )


def _Apnd_to_File(   fm_box ) : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _Apnd_to_File : Not Done Yet' )
    messagebox.showinfo( '_Apnd_to_File' , 'This function is not done yet.' )


def _Save_to_Clip(   fm_box ) : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _Save_to_Clip : Not Done Yet' )
    messagebox.showinfo( '_Save_to_Clip' , 'This function is not done yet.' )


def _Apnd_to_Clip(   fm_box ) : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _Apnd_to_Clip : Not Done Yet' )
    messagebox.showinfo( '_Apnd_to_Clip' , 'This function is not done yet.' )


def _folder_picker( to_box ) :

    '''Not Done. Not Used'''

    print( f'_file_picker( "{to_box}" )')

    file_get = rf'{filedialog.askdirectory(title="Select Folder")}'


def _Open_from_File( to_box , to_clear ) :

    print( f'_Open_from_File( "{to_box}" , "{to_clear}" )')

    file_get = rf'{filedialog.askopenfilename( title="Select One File" , filetypes=(("Text Files", "*.txt *.log *.json *.jsonl *.ndjson *.jsonld *.xml *.csv *.nmap *.gnmap" ),("Scripts", "*.pl *.rb *.py *.sh *.css *.js *.htm *.html"),("All Files", "*.*")))}'
    
    if not os.path.isfile( file_get ) :

        print( f'# ERR  # _Open_from_File # isfile fail : {file_get}' )
        messagebox.showinfo( f'# ERR  # _Open_from_File # isfile fail : {file_get}' )
    
    else :

        if to_clear : _clear_box( to_box )

        if   file_get.endswith( ".gz" ) : fh = gzip.open( file_get , "rb" )
        else                            : fh =      open( file_get , "r"  )

        box[ to_box ].insert( "end" , "".join( fh.readlines() ) )


def _file_box_set( to_parent , to_box ) :

    '''
    File select dialoge. Does not open files. Only gets file paths and 
    sets them in FileA or FileB for futute use through another get 
    function.
    '''

    #todo : finish
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _file_box_set : finish' )

    print( f'_file_box_set( "{to_parent}" , "{to_box}" )')

    file_mget = rf'{filedialog.askopenfilename( parent=abc[ to_parent ] , title="Select One or More Files" , multiple = True , filetypes=(("Text Files", "*.txt *.log *.json *.jsonl *.ndjson *.jsonld *.xml *.csv"),("Scripts", "*.pl *.rb *.py *.sh *.css *.js *.htm *.html"),("All Files", "*.*")))}'

    print( f'_file_box_set file_mget( "{file_mget}" )')

    if file_mget : print( f'_file_box_set file_mget( "{file_mget}" )')
    if file_mget : print( f'_file_box_set type( "{type(file_mget)}" )')
    if file_mget : print( f'_file_box_set file_mget.split( "{file_mget.split()}" )')

    if file_mget :
        for x in re.findall( r'\'(..*?)\'', file_mget ) :
            if x and x.strip() : print( f'{x}' )


def _file_box_get( to_parent , to_box ) : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _file_box_get : Not Done Yet' )
    messagebox.showinfo( '_file_box_get' , 'This function is not done yet.' )


def _trim_blank_lines( **kwargs ) :  ## 327198c34e3fa4ef2ecfb922d4b66e75 # 2024-04-02 10:01:00 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _trim_blank_lines( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    to_box = fm_box

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()
    lst_fm = [ x.strip() for x in lst_fm if x.strip() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _trim_trailing_spaces( **kwargs ) :  ## 982d7c65b393c6a82e2d359d7438a114 # 2024-04-02 10:00:45 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _trim_trailing_spaces( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.rstrip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _trim_leading_spaces( **kwargs ) :  ## c9d97e1b2a29295882cc86f8c8733805 # 2024-04-02 10:00:31 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _trim_leading_spaces( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.lstrip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _deduplicate_lines( **kwargs ) :  ## 821b1ffd087740381a2013ec05ed2215 # 2024-04-02 10:00:13 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )
    
    #todo: Maintain order
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _deduplicate_lines : Maintain order' )
    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _deduplicate_lines( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    set_fm     = set()
    set_fm_add = set_fm.add

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

    lst_fm = [ x for x in lst_fm if not ( x in set_fm or set_fm_add( x ) ) ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _sort_lines( **kwargs ) :  ## 4e89854aa2039992cbfe9e79757b9091 # 2024-10-14 16:40:39 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )
    order  = kwargs.get( "order"  , "AZ" )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _sort_lines( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" , "order" : "{order}" }} )' )

    sorted_lines = []
    if   order == "AZ" : sorted_lines = sorted( box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() , key=str.casefold                )
    elif order == "ZA" : sorted_lines = sorted( box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() , key=str.casefold , reverse=True )

    _clear_box( to_box )

    for x in sorted_lines : box[ to_box ].insert( "end" , f"{x}\n" )


def _change_case_upper( **kwargs ) :  ## fd28abd581639dcbf13b0bf5e49b02b4 # 2024-04-02 09:59:41 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _change_case_upper( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.upper() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _change_case_lower( **kwargs ) :  ## 02df1c55b2eec1128dee5e52d23739a1 # 2024-04-02 09:59:28 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _change_case_lower( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.lower() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _change_case_casefold( **kwargs ) :  ## 25ea6609a8c87b78cc9fd111ea838c24 # 2024-04-02 09:59:16 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _change_case_casefold( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.casefold() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _change_case_title( **kwargs ) :  ## 3dcc6a8d98a72d0f0dd0c504b78731a2 # 2024-04-02 09:59:03 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _change_case_title( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.title() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _apnd_to_box_from_box( **kwargs ) :  ## be8ffcf102c5862221b7b678b1b3a1c9 # 2024-04-02 09:58:38 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , "C" )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _apnd_to_box_from_box( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _swap_to_box_from_box( **kwargs ) :  ## af35998a51f662b4b4b6834f033f3692 # 2024-04-02 09:58:10 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , "C" )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _swap_to_box_from_box( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()
    lst_to = box[ to_box ].get( "1.0" , 'end-1c' ).splitlines()

    _clear_box( fm_box )
    _clear_box( to_box )

    for x in lst_to : box[ fm_box ].insert( "end" , f"{x}\n" )
    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _move_to_box_from_box( **kwargs ) :  ## 885d377140f9c4cd6f7d7b447eba9d3b # 2024-04-02 09:57:55 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , "C" )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _move_to_box_from_box( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

    if fm_box :

        _clear_box( fm_box )
        _clear_box( to_box )

        for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


# endregion  # ABC Window Functions ####################################







########################################################################
##                           Other Helpers                            ##
########################################################################

# region     # Other Helpers ###########################################


# endregion  # Other Helpers ###########################################







###########################################################################################################


###########################################################################################################
#                                                                                                         #
#             #     # ####### #     # #     #           ###   ####### ####### #     #  #####              #
#             ##   ## #       ##    # #     #            #       #    #       ##   ## #     #             #
#             # # # # #       # #   # #     #            #       #    #       # # # # #                   #
#             #  #  # #####   #  #  # #     #            #       #    #####   #  #  #  #####              #
#             #     # #       #   # # #     #            #       #    #       #     #       #             #
#             #     # #       #    ## #     #            #       #    #       #     # #     #             #
#             #     # ####### #     #  #####            ###      #    ####### #     #  #####              #
#                                                                                                         #
###########################################################################################################


###########################################################################################################



###########################################################################################################
#                                                                                                         #
#                                         #######                                                         #
#                                         #       # #      ######                                         #
#                                         #       # #      #                                              #
#                                         #####   # #      #####                                          #
#                                         #       # #      #                                              #
#                                         #       # #      #                                              #
#                                         #       # ###### ######                                         #
#                                                                                                         #
###########################################################################################################




########################################################################
##                             File Menu                              ##
########################################################################

# region     ## File Menu ##############################################

def menubar_file() :  ## 88dab9245731a5bf5e71605f10da3641 # 2024-10-14 17:24:48 #

    ## Main Title Menu #################################################

    abc[  "menubar" ] = Menu( abc[  "main_window" ] )

    abc[  "main_window" ].config( menu = abc[  "menubar" ] )

    ####################################################################
    #                            File Menu                             #
    ####################################################################

    abc[  "menubar_file" ] = Menu( abc[  "menubar" ] , tearoff = 1 ) ; abc[  "menubar" ].add_cascade( label = "File" , menu = abc[  "menubar_file" ] )

    abc[  "menubar_file" ].add_command( label = 'Exit' , command = abc[  "main_window" ].destroy )

# endregion  ## File Menu ##############################################







###############################################################################################################
#                                                                                                             #
#                              #######                                                                        #
#                              #     # #####  ##### #  ####  #    #  ####                                     #
#                              #     # #    #   #   # #    # ##   # #                                         #
#                              #     # #    #   #   # #    # # #  #  ####                                     #
#                              #     # #####    #   # #    # #  # #      #                                    #
#                              #     # #        #   # #    # #   ## #    #                                    #
#                              ####### #        #   #  ####  #    #  ####                                     #
#                                                                                                             #
###############################################################################################################
                                            



########################################################################
##                            Options Menu                            ##
########################################################################

#region    ## Options Menu #############################################

def menubar_options() :  ## 3c3a1e90516701af743cfd822ec123dc # 2024-10-14 17:26:47 #

    abc[  "menubar_options"  ] = Menu( abc[  "menubar" ] , tearoff = 1 ) ; abc[  "menubar" ].add_cascade( label = "Options"   , menu = abc[  "menubar_options"  ] )

    ## Options Menu : Default Record Separators ########################

    abc[  "options_record_separator" ] = StringVar()
    abc[  "options_record_separator" ].set( gopts[ "record_separator" ] )

    abc[  "menubar_options_rec_sep"  ] = Menu( abc[  "menubar_options" ] , tearoff = 1 )

    abc[  "menubar_options" ].add_cascade( font = "TkFixedFont" , label = "Default Record Separator" , menu = abc[  "menubar_options_rec_sep" ] )

    abc[  "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Newline         \\n"            , value = '\n'       , variable=abc[ "options_record_separator" ] )
    abc[  "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "CRLF            \\r\\n"         , value = '\r\n'     , variable=abc[ "options_record_separator" ] )
    abc[  "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Double Newline  \\n\\n"         , value = '\n\n'     , variable=abc[ "options_record_separator" ] )
    abc[  "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Double CRLF     \\r\\n\\r\\n"   , value = '\r\n\r\n' , variable=abc[ "options_record_separator" ] )
    abc[  "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Pound LF        #\\n"           , value = '#\n'      , variable=abc[ "options_record_separator" ] )
    abc[  "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Bang LF         !\\n"           , value = '!\n'      , variable=abc[ "options_record_separator" ] )

    ## Options Menu : Default Column Separator #########################

    abc[  "options_column_separator" ] = StringVar()
    abc[  "options_column_separator" ].set( gopts[ "column_separator" ] )

    abc[  "menubar_options_col_sep"  ] = Menu( abc[  "menubar_options" ] , tearoff = 1 )

    abc[  "menubar_options" ].add_cascade( font = "TkFixedFont" , label = "Default Column Separator" , menu = abc[  "menubar_options_col_sep" ] )

    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Comma           \",\""     , value = ','     , variable=abc[ "options_column_separator" ] )
    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Comma Space     \", \""    , value = ', '    , variable=abc[ "options_column_separator" ] )
    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Pipe            \"|\""     , value = '|'     , variable=abc[ "options_column_separator" ] )
    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Carat           \"^\""     , value = '^'     , variable=abc[ "options_column_separator" ] )
    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Spaced ORs      \" OR \""  , value = ' OR '  , variable=abc[ "options_column_separator" ] )
    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Spaced ||s      \" || \""  , value = ' OR '  , variable=abc[ "options_column_separator" ] )
    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Spaced ANDs     \" AND \"" , value = ' AND ' , variable=abc[ "options_column_separator" ] )
    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Spaced &&s      \" && \""  , value = ' AND ' , variable=abc[ "options_column_separator" ] )
    abc[  "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Cherries        \"@@@\""   , value = '@@@'   , variable=abc[ "options_column_separator" ] )

    ## Options Menu : Readlines Options ################################

    abc[  "options_trim_leading_spaces"  ] = BooleanVar()
    abc[  "options_trim_trailing_spaces" ] = BooleanVar()
    abc[  "options_trim_blank_lines"     ] = BooleanVar()
    abc[  "options_read_in_boxes_upper"  ] = BooleanVar()
    abc[  "options_read_in_boxes_lower"  ] = BooleanVar()
    abc[  "options_read_in_boxes_dedupe" ] = BooleanVar()

    abc[  "options_trim_leading_spaces"  ].set( gopts[ "trim_leading_spaces"  ] )
    abc[  "options_trim_trailing_spaces" ].set( gopts[ "trim_trailing_spaces" ] )
    abc[  "options_trim_blank_lines"     ].set( gopts[ "trim_blank_lines"     ] )
    abc[  "options_read_in_boxes_upper"  ].set( gopts[ "read_in_boxes_upper"  ] )
    abc[  "options_read_in_boxes_lower"  ].set( gopts[ "read_in_boxes_lower"  ] )
    abc[  "options_read_in_boxes_dedupe" ].set( gopts[ "read_in_boxes_dedupe" ] )

    abc[  "menubar_options"  ].add_checkbutton( label = "Trim leading spaces on read"  , onvalue=1 , offvalue=0 , variable=abc[ "options_trim_leading_spaces"  ] )
    abc[  "menubar_options"  ].add_checkbutton( label = "Trim trailing spaces on read" , onvalue=1 , offvalue=0 , variable=abc[ "options_trim_trailing_spaces" ] )
    abc[  "menubar_options"  ].add_checkbutton( label = "Trim blank lines on read"     , onvalue=1 , offvalue=0 , variable=abc[ "options_trim_blank_lines"     ] )
    abc[  "menubar_options"  ].add_checkbutton( label = "Uppercase on read"            , onvalue=1 , offvalue=0 , variable=abc[ "options_read_in_boxes_upper"  ] )
    abc[  "menubar_options"  ].add_checkbutton( label = "Lowercase on read"            , onvalue=1 , offvalue=0 , variable=abc[ "options_read_in_boxes_lower"  ] )
    abc[  "menubar_options"  ].add_checkbutton( label = "Dedupe on read"               , onvalue=1 , offvalue=0 , variable=abc[ "options_read_in_boxes_dedupe" ] )

#endregion ## Options Menu #############################################






###############################################################################################################
#                                                                                                             #
#                                            #    ######   #####                                              #
#                                           # #   #     # #     #                                             #
#                                          #   #  #     # #                                                   #
#                                         #     # ######  #                                                   #
#                                         ####### #     # #                                                   #
#                                         #     # #     # #     #                                             #
#                                         #     # ######   #####                                              #
#                                                                                                             #
###############################################################################################################




########################################################################
##                              ABC Menu                              ##
########################################################################

# region     ## ABC Menu ###############################################

def menubar_abc() :  ## d03b39ed1711ac91cba1dd9d29b947cb # 2024-10-14 17:27:08 #

    abc[  "menubar_abc" ] = Menu( abc[  "menubar" ] , tearoff = 1 )
    
    abc[  "menubar" ].add_cascade( label = "ABC" , menu = abc[  "menubar_abc" ] )

    abc[  "menubar_abc" ].add_command( font = "TkFixedFont" , label = 'Clear All Boxes' , command = lambda: _clear_boxes() )
    abc[  "menubar_abc" ].add_command( font = "TkFixedFont" , label = 'Clear Box A'     , command = lambda: _clear_box( "A" ) )
    abc[  "menubar_abc" ].add_command( font = "TkFixedFont" , label = 'Clear Box B'     , command = lambda: _clear_box( "B" ) )
    abc[  "menubar_abc" ].add_command( font = "TkFixedFont" , label = 'Clear Box C'     , command = lambda: _clear_box( "C" ) )

    abc[  "menubar_abc" ].add_separator()

    ####################################################################
    ##                        ABC Menu: Box A                         ##
    ####################################################################

    abc[  "menubar_abc__box_a"  ] = Menu( abc[  "menubar_abc" ] , tearoff = 1 )
    abc[  "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box A" , menu = abc[  "menubar_abc__box_a" ] )

    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Open File into Box'               , command = lambda: _Open_from_File( "A" , 1 ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Open File Append to Box'          , command = lambda: _Open_from_File( "A" , 0 ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Trim blank lines and spaces'      , command = lambda: _trim_blank_lines(     **{ "fm_box" : "A"                  } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Trim trailing whitespace'         , command = lambda: _trim_trailing_spaces( **{ "fm_box" : "A"                  } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Trim leading whitespace'          , command = lambda: _trim_leading_spaces(  **{ "fm_box" : "A"                  } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Sort lines ascending order'       , command = lambda: _sort_lines(           **{ "fm_box" : "A" , "order" : "AZ" } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Sort lines descending order'      , command = lambda: _sort_lines(           **{ "fm_box" : "A" , "order" : "ZA" } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Dedupe Lines'                     , command = lambda: _deduplicate_lines(    **{ "fm_box" : "A"                  } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Change data to upper case'        , command = lambda: _change_case_upper(    **{ "fm_box" : "A"                  } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Change data to lower case'        , command = lambda: _change_case_lower(    **{ "fm_box" : "A"                  } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Change data to casefold case'     , command = lambda: _change_case_casefold( **{ "fm_box" : "A"                  } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Change data to title case'        , command = lambda: _change_case_title(    **{ "fm_box" : "A"                  } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Swap Box A contents with Box B'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Swap Box A contents with Box C'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Move Box A contents to Box B'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Move Box A contents to Box C'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Append Box A contents to Box B'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Append Box A contents to Box C'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) )
    abc[  "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Clear Box'                        , command = lambda: _clear_box(                           "A"                    ) )
    #abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Save to File'                     , command = lambda: _not_done_yet() )
    #abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Append to File'                   , command = lambda: _not_done_yet() )

    ####################################################################
    ##              ABC Menu: Box A : Sorting Functions               ##
    ####################################################################

    abc[  "menubar_abc__box_a_sort"  ] = Menu( abc[  "menubar_abc__box_a" ] , tearoff = 1 )
    abc[  "menubar_abc__box_a" ].add_cascade( font = "TkFixedFont" , label = "More Sorting Functions" , menu = abc[  "menubar_abc__box_a_sort" ] )

    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. A to Z. Ignore Case.'                , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "AZ"   , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. A to Z.'                             , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "AZ"   , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Z to A. Ignore Case.'                , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "ZA"   , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Z to A.'                             , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "ZA"   , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. A to Z. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "LSAZ" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. A to Z.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "LSAZ" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. Z to A. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "LSZA" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. Z to A.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "LSZA" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. A to Z. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "SLAZ" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. A to Z.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "SLAZ" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. Z to A. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "SLZA" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. Z to A.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "lines"  , "sort_order" : "SLZA" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort IP Addresses. Low to High.'                 , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "ipaddr" , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort IP Addresses. High to Low.'                 , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "ipaddr" , "sort_order" : "ZA"                     } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Domain Names. A to Z. Ignore Case.'         , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "domain" , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Domain Names. Z to A. Ignore Case.'         , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "domain" , "sort_order" : "ZA"                     } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Email Addresses. A to Z. Ignore Case.'      , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "email"  , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_a_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Email Addresses. Z to A. Ignore Case.'      , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "A" , "sort_what"  : "email"  , "sort_order" : "ZA"                     } ) )


    ####################################################################
    ##                        ABC Menu: Box B                         ##
    ####################################################################

    abc[  "menubar_abc__box_b"  ] = Menu( abc[  "menubar_abc" ] , tearoff = 1 )
    abc[  "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box B" , menu = abc[  "menubar_abc__box_b" ] )

    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Open File into Box'               , command = lambda: _Open_from_File( "B" , 1 ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Open File Append to Box'          , command = lambda: _Open_from_File( "B" , 0 ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Trim blank lines and spaces'      , command = lambda: _trim_blank_lines(     **{ "fm_box" : "B"                  } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Trim trailing whitespace'         , command = lambda: _trim_trailing_spaces( **{ "fm_box" : "B"                  } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Trim leading whitespace'          , command = lambda: _trim_leading_spaces(  **{ "fm_box" : "B"                  } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Sort lines ascending order'       , command = lambda: _sort_lines(           **{ "fm_box" : "B" , "order" : "AZ" } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Sort lines descending order'      , command = lambda: _sort_lines(           **{ "fm_box" : "B" , "order" : "ZA" } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Dedupe Lines'                     , command = lambda: _deduplicate_lines(    **{ "fm_box" : "B"                  } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Change data to upper case'        , command = lambda: _change_case_upper(    **{ "fm_box" : "B"                  } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Change data to lower case'        , command = lambda: _change_case_lower(    **{ "fm_box" : "B"                  } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Change data to casefold case'     , command = lambda: _change_case_casefold( **{ "fm_box" : "B"                  } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Change data to title case'        , command = lambda: _change_case_title(    **{ "fm_box" : "B"                  } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Swap Box B contents with Box A'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Swap Box B contents with Box C'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Move Box B contents to Box A'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Move Box B contents to Box C'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Append Box B contents to Box A'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Append Box B contents to Box C'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) )
    abc[  "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Clear Box'                        , command = lambda: _clear_box(                           "B"                    ) )
    #abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Save to File'                     , command = lambda: _not_done_yet() )
    #abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Append to File'                   , command = lambda: _not_done_yet() )

    ####################################################################
    ##              ABC Menu: Box B : Sorting Functions               ##
    ####################################################################

    abc[  "menubar_abc__box_b_sort"  ] = Menu( abc[  "menubar_abc__box_b" ] , tearoff = 1 )
    abc[  "menubar_abc__box_b" ].add_cascade( font = "TkFixedFont" , label = "More Sorting Functions" , menu = abc[  "menubar_abc__box_b_sort" ] )

    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. A to Z. Ignore Case.'                , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "AZ"   , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. A to Z.'                             , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "AZ"   , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Z to A. Ignore Case.'                , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "ZA"   , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Z to A.'                             , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "ZA"   , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. A to Z. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "LSAZ" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. A to Z.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "LSAZ" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. Z to A. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "LSZA" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. Z to A.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "LSZA" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. A to Z. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "SLAZ" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. A to Z.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "SLAZ" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. Z to A. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "SLZA" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. Z to A.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "lines"  , "sort_order" : "SLZA" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort IP Addresses. Low to High.'                 , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "ipaddr" , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort IP Addresses. High to Low.'                 , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "ipaddr" , "sort_order" : "ZA"                     } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Domain Names. A to Z. Ignore Case.'         , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "domain" , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Domain Names. Z to A. Ignore Case.'         , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "domain" , "sort_order" : "ZA"                     } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Email Addresses. A to Z. Ignore Case.'      , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "email"  , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_b_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Email Addresses. Z to A. Ignore Case.'      , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "B" , "sort_what"  : "email"  , "sort_order" : "ZA"                     } ) )


    ####################################################################
    ##                        ABC Menu: Box C                         ##
    ####################################################################

    abc[  "menubar_abc__box_c"  ] = Menu( abc[  "menubar_abc" ] , tearoff = 1 )
    abc[  "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box C" , menu = abc[  "menubar_abc__box_c" ] )

    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Open File into Box'               , command = lambda: _Open_from_File( "C" , 1 ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Open File Append to Box'          , command = lambda: _Open_from_File( "C" , 0 ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Trim blank lines and spaces'      , command = lambda: _trim_blank_lines(     **{ "fm_box" : "C"                  } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Trim trailing whitespace'         , command = lambda: _trim_trailing_spaces( **{ "fm_box" : "C"                  } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Trim leading whitespace'          , command = lambda: _trim_leading_spaces(  **{ "fm_box" : "C"                  } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Sort lines ascending order'       , command = lambda: _sort_lines(           **{ "fm_box" : "C" , "order" : "AZ" } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Sort lines descending order'      , command = lambda: _sort_lines(           **{ "fm_box" : "C" , "order" : "ZA" } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Dedupe Lines'                     , command = lambda: _deduplicate_lines(    **{ "fm_box" : "C"                  } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Change data to upper case'        , command = lambda: _change_case_upper(    **{ "fm_box" : "C"                  } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Change data to lower case'        , command = lambda: _change_case_lower(    **{ "fm_box" : "C"                  } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Change data to casefold case'     , command = lambda: _change_case_casefold( **{ "fm_box" : "C"                  } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Change data to title case'        , command = lambda: _change_case_title(    **{ "fm_box" : "C"                  } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Swap Box C contents with Box A'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Swap Box C contents with Box B'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Move Box C contents to Box A'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Move Box C contents to Box B'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Append Box C contents to Box A'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Append Box C contents to Box B'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) )
    abc[  "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Clear Box'                        , command = lambda: _clear_box(                           "C"                    ) )
    #abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Save to File'                     , command = lambda: _not_done_yet() )
    #abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Append to File'                   , command = lambda: _not_done_yet() )

    ####################################################################
    ##              ABC Menu: Box C : Sorting Functions               ##
    ####################################################################

    abc[  "menubar_abc__box_c_sort"  ] = Menu( abc[  "menubar_abc__box_c" ] , tearoff = 1 )
    abc[  "menubar_abc__box_c" ].add_cascade( font = "TkFixedFont" , label = "More Sorting Functions" , menu = abc[  "menubar_abc__box_c_sort" ] )

    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. A to Z. Ignore Case.'                , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "AZ"   , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. A to Z.'                             , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "AZ"   , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Z to A. Ignore Case.'                , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "ZA"   , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Z to A.'                             , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "ZA"   , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. A to Z. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "LSAZ" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. A to Z.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "LSAZ" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. Z to A. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "LSZA" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Long to Short. Z to A.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "LSZA" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. A to Z. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "SLAZ" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. A to Z.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "SLAZ" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. Z to A. Ignore Case.' , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "SLZA" , "sort_case" : 0 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort lines. Short to Long. Z to A.'              , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "lines"  , "sort_order" : "SLZA" , "sort_case" : 1 } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort IP Addresses. Low to High.'                 , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "ipaddr" , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort IP Addresses. High to Low.'                 , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "ipaddr" , "sort_order" : "ZA"                     } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Domain Names. A to Z. Ignore Case.'         , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "domain" , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Domain Names. Z to A. Ignore Case.'         , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "domain" , "sort_order" : "ZA"                     } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Email Addresses. A to Z. Ignore Case.'      , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "email"  , "sort_order" : "AZ"                     } ) )
    abc[  "menubar_abc__box_c_sort" ].add_command( font = "TkFixedFont" , label = 'Sort Email Addresses. Z to A. Ignore Case.'      , command = lambda: abc__tops__sort_lines( **{ "fm_box" : "C" , "sort_what"  : "email"  , "sort_order" : "ZA"                     } ) )


    ####################################################################
    ##                       ABC Menu: Box Swap                       ##
    ####################################################################

    abc[  "menubar_abc__swap"   ] = Menu( abc[  "menubar_abc" ] , tearoff = 1 )
    abc[  "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box Swap" , menu = abc[  "menubar_abc__swap" ] )

    abc[  "menubar_abc__swap" ].add_command( font = "TkFixedFont" , label = 'Swap Box A contents with Box B'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_swap("A" , "B")   ; } ]
    abc[  "menubar_abc__swap" ].add_command( font = "TkFixedFont" , label = 'Swap Box A contents with Box C'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_swap("A" , "C")   ; } ]
    abc[  "menubar_abc__swap" ].add_command( font = "TkFixedFont" , label = 'Swap Box B contents with Box A'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_swap("B" , "A")   ; } ]
    abc[  "menubar_abc__swap" ].add_command( font = "TkFixedFont" , label = 'Swap Box B contents with Box C'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_swap("B" , "C")   ; } ]
    abc[  "menubar_abc__swap" ].add_command( font = "TkFixedFont" , label = 'Swap Box C contents with Box A'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_swap("C" , "A")   ; } ]
    abc[  "menubar_abc__swap" ].add_command( font = "TkFixedFont" , label = 'Swap Box C contents with Box B'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_swap("C" , "B")   ; } ]

    ####################################################################
    ##                       ABC Menu: Box Move                       ##
    ####################################################################

    abc[  "menubar_abc__move"   ] = Menu( abc[  "menubar_abc" ] , tearoff = 1 )
    abc[  "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box Move" , menu = abc[  "menubar_abc__move"   ] )

    abc[  "menubar_abc__move" ].add_command( font = "TkFixedFont" , label = 'Move Box A contents to Box B'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_move("A" , "B")   ; } ]
    abc[  "menubar_abc__move" ].add_command( font = "TkFixedFont" , label = 'Move Box A contents to Box C'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_move("A" , "C")   ; } ]
    abc[  "menubar_abc__move" ].add_command( font = "TkFixedFont" , label = 'Move Box B contents to Box A'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_move("B" , "A")   ; } ]
    abc[  "menubar_abc__move" ].add_command( font = "TkFixedFont" , label = 'Move Box B contents to Box C'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_move("B" , "C")   ; } ]
    abc[  "menubar_abc__move" ].add_command( font = "TkFixedFont" , label = 'Move Box C contents to Box A'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_move("C" , "A")   ; } ]
    abc[  "menubar_abc__move" ].add_command( font = "TkFixedFont" , label = 'Move Box C contents to Box B'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_move("C" , "B")   ; } ]

    ####################################################################
    ##                      ABC Menu: Box Append                      ##
    ####################################################################

    abc[  "menubar_abc__apnd"   ] = Menu( abc[  "menubar_abc" ] , tearoff = 1 )
    abc[  "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box Append" , menu = abc[  "menubar_abc__apnd" ] )

    abc[  "menubar_abc__apnd" ].add_command( font = "TkFixedFont" , label = 'Append Box A contents to Box B'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_append("A" , "B")  ; } ]
    abc[  "menubar_abc__apnd" ].add_command( font = "TkFixedFont" , label = 'Append Box A contents to Box C'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_append("A" , "C")  ; } ]
    abc[  "menubar_abc__apnd" ].add_command( font = "TkFixedFont" , label = 'Append Box B contents to Box A'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_append("B" , "A")  ; } ]
    abc[  "menubar_abc__apnd" ].add_command( font = "TkFixedFont" , label = 'Append Box B contents to Box C'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_append("B" , "C")  ; } ]
    abc[  "menubar_abc__apnd" ].add_command( font = "TkFixedFont" , label = 'Append Box C contents to Box A'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_append("C" , "A")  ; } ]
    abc[  "menubar_abc__apnd" ].add_command( font = "TkFixedFont" , label = 'Append Box C contents to Box B'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_append("C" , "B")  ; } ]

    ####################################################################
    ##                        ABC Menu: File A                        ##
    ####################################################################

    abc[  "menubar_abc__file_a" ] = Menu( abc[  "menubar_abc" ] , tearoff = 1 )
    abc[  "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "File A" , menu = abc[  "menubar_abc__file_a" ] )

    abc[  "menubar_abc__file_a" ].add_command( font = "TkFixedFont" , label = 'Append File A and File B to Box A' , command = lambda: _not_done_yet() )
    abc[  "menubar_abc__file_a" ].add_command( font = "TkFixedFont" , label = 'Diff File A and File B to Box C'   , command = lambda: _not_done_yet() )

    ####################################################################
    ##                        ABC Menu: File B                        ##
    ####################################################################

    abc[  "menubar_abc__file_b" ] = Menu( abc[  "menubar_abc" ] , tearoff = 1 )
    abc[  "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "File B" , menu = abc[  "menubar_abc__file_b"   ] )

    abc[  "menubar_abc__file_b" ].add_command( font = "TkFixedFont" , label = 'Append File A and File B to Box A' , command = lambda: _not_done_yet() )
    abc[  "menubar_abc__file_b" ].add_command( font = "TkFixedFont" , label = 'Diff File A and File B to Box C'   , command = lambda: _not_done_yet() )

# endregion  ## ABC Menu ###########################################











###############################################################################################################
#                                                                                                             #
#                              #####  ####### #     # ######     #    ######  #######                         #
#                             #     # #     # ##   ## #     #   # #   #     # #                               #
#                             #       #     # # # # # #     #  #   #  #     # #                               #
#                             #       #     # #  #  # ######  #     # ######  #####                           #
#                             #       #     # #     # #       ####### #   #   #                               #
#                             #     # #     # #     # #       #     # #    #  #                               #
#                              #####  ####### #     # #       #     # #     # #######                         #
#                                                                                                             #
###############################################################################################################




########################################################################
##                            Compare Menu                            ##
########################################################################

# region     ## Compare Menu ###########################################

def menubar_compare() :  ## 80a128fbc9c3fa9ba506c46bf8d83298 # 2024-10-14 17:30:22 #

    abc[  "menubar_compare"  ] = Menu( abc[  "menubar" ] , tearoff = 1 ) ; abc[  "menubar" ].add_cascade( label = "Compare"   , menu = abc[  "menubar_compare"  ] )

    abc[  "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'A + B to C (Merge A and B)'                 , command = lambda: abc__compare__AB_union(     "A" , "B" , "C" ) )
    abc[  "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'A - B to C (Take B from A)'                 , command = lambda: abc__compare__AB_minus(     "A" , "B" , "C" ) )
    abc[  "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'B - A to C (Take A from B)'                 , command = lambda: abc__compare__AB_minus(     "B" , "A" , "C" ) )
    abc[  "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'AB to C (In both A and B)'                  , command = lambda: abc__compare__AB_intersect( "A" , "B" , "C" ) )
    abc[  "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'A + B - AB to C (In A or B but not both)'   , command = lambda: abc__compare__AB_symdiff(   "A" , "B" , "C" ) )
    abc[  "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'Labeled Diff A and B'                       , command = lambda: abc__compare__AB_diff(      "A" , "B" , "C" ) )
    abc[  "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'Count Lines in Each Box'                    , command = lambda: abc__cardinality_all() )

    ####################################################################

    abc[  "menubar_compare" ].add_separator()

    ####################################################################

    abc[  "menubar_compare__more"  ] = Menu( abc[  "menubar_compare" ] , tearoff = 1 )
    abc[  "menubar_compare" ].add_cascade( font = "TkFixedFont" , label = "More" , menu = abc[  "menubar_compare__more"  ] )

    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = 'A & B                 > Box C' , command = lambda: abc__compare__AB_union(     "A" , "B" , "C" ) )
    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = 'A - B                 > Box C' , command = lambda: abc__compare__AB_minus(     "A" , "B" , "C" ) )
    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = 'B - A                 > Box C' , command = lambda: abc__compare__AB_minus(     "B" , "A" , "C" ) )
    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = 'A | B                 > Box C' , command = lambda: abc__compare__AB_intersect( "A" , "B" , "C" ) )
    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = 'A \u0394 B = ( A - B ) & ( B - A )  > Box C' , command = lambda: abc__compare__AB_symdiff(   "A" , "B" , "C" ) )
    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = 'A X B (Cross Product) > Box C' , command = lambda: abc__compare__AB_cross_prod( "A" , "B" , "C" ) )
    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = '|A|         '                  , command = lambda: abc__cardinality_one( "A" ) )
    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = '|B|         '                  , command = lambda: abc__cardinality_one( "B" ) )
    abc[  "menubar_compare__more" ].add_command( font = "TkFixedFont" , label = '|C|         '                  , command = lambda: abc__cardinality_one( "C" ) )

# endregion  ## Compare Menu ###########################################





########################################################################
#                          Compare Functions                           #
########################################################################

# region     # Compare Functions #######################################

def abc__compare__AB_union( box_a , box_b , to_box ) :  ## 22af3553312de5783cef2d925f396ac1 # 2024-10-14 17:31:56 #

    print( f'abc__compare__AB_union( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )

    for x in set_a.union( set_b ) :
        if x and x.strip() : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__compare__AB_intersect( box_a , box_b , to_box ) :  ## 4f95caeff18a37e23c1ea393e324a7d0 # 2024-10-14 17:32:13 #

    print( f'abc__compare__AB_intersect( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )

    for x in set_a.intersection( set_b ) :
        if x and x.strip() : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__compare__AB_minus( box_a , box_b , to_box ) :  ## 40b4f68b557c6ae03717ccd6bab578c7 # 2024-10-14 17:32:46 #

    print( f'abc__compare__AB_minus( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )

    for x in set_a.difference( set_b ) :
        if x and x.strip() : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__compare__AB_diff( box_a , box_b , to_box ) :  ## d17e902cbf09d2f69005ad6d86c3ff34 # 2024-10-14 17:33:05 #

    print( f'abc__compare__AB_diff( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )
    
    cmnt = "In A but not B" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    for x in set_a.difference( set_b ) : box[ to_box ].insert( "end" , f"{x}\n" )

    cmnt = "In B but not B" ; box[ to_box ].insert( "end" , f'\n{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    for x in set_b.difference( set_a ) : box[ to_box ].insert( "end" , f"{x}\n" )
    
    cmnt = "In both A and B" ; box[ to_box ].insert( "end" , f'\n{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    for x in set_a.intersection( set_b ) : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__compare__AB_symdiff( box_a , box_b , to_box ) :  ## 5ce5ac8c7baa7a39f9d190d024f9c0ee # 2024-10-14 17:33:36 #

    print( f'abc__compare__AB_symdiff( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )

    for x in set_a.symmetric_difference( set_b ) :
        if x and x.strip() : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__cardinality_one( fm_box ) :  ## 3bf24bd2496088ca5954514bdb9073a0 # 2024-10-14 17:33:52 #

    print( f'abc__cardinality_one( "{fm_box}" )')

    lst_a = [ x.strip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ]

    messagebox.showinfo( 'Cardinality' , f'{len( lst_a ):14,d} : Total lines in Box {fm_box}\n{len( set( lst_a ) ):14,d} : Total unique lines in Box {fm_box}' )


def abc__cardinality_all() :  ## f4298839cc382008238a8e8f15575a0e # 2024-10-14 17:34:36 #

    print( f'abc__cardinality_all( )')

    lst_a = [ x.strip() for x in box[ "A" ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ]
    lst_b = [ x.strip() for x in box[ "B" ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ]
    lst_c = [ x.strip() for x in box[ "C" ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ]

    set_a = set( lst_a )
    set_b = set( lst_a )
    set_c = set( lst_a )

    cnt_lst_a = len( lst_a )
    cnt_lst_b = len( lst_b )
    cnt_lst_c = len( lst_c )

    cnt_set_a = len( set_a )
    cnt_set_b = len( set_b )
    cnt_set_c = len( set_c )

    cnt_lst_z = cnt_lst_a + cnt_lst_b + cnt_lst_c
    cnt_set_z = len( set_a | set_b | set_c )

    message_text  = \
          f'{cnt_lst_a:14,d} : Total lines in Box A\n{cnt_set_a:14,d} : Total unique lines in Box A\n' \
        + f'{cnt_lst_b:14,d} : Total lines in Box B\n{cnt_set_b:14,d} : Total unique lines in Box B\n' \
        + f'{cnt_lst_c:14,d} : Total lines in Box C\n{cnt_set_c:14,d} : Total unique lines in Box C\n' \
        + "\n" \
        + f'{cnt_lst_z:14,d} : Total lines in All Boxes\n{cnt_set_z:14,d} : Total unique lines in All Boxes\n'

    messagebox.showinfo( 'Cardinality' , message_text )


def abc__compare__AB_cross_prod( box_a , box_b , to_box ) :  ## ff9ea25749cff04b68a46bcb4c41975e # 2024-10-14 17:34:52 #

    set_a = set( box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() )
    set_b = set( box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() )

    column_separator = gopts[ "column_separator" ]

    _clear_box( to_box )

    for v1 , v2 in [ ( x , y ) for x in set_a for y in set_b ] :
        box[ to_box ].insert( "end" , f"{v1}{column_separator}{v2}\n" )


def U__compare__A_minus_BorC() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # U__compare__A_minus_BorC : Not Done Yet' )
    messagebox.showinfo( 'U__compare__A_minus_BorC' , 'This function is not done yet.' )


def U__compare__A_minus_BandC() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # U__compare__A_minus_BandC : Not Done Yet' )
    messagebox.showinfo( 'U__compare__A_minus_BandC' , 'This function is not done yet.' )


def U__compare__AorB_minus_C() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # U__compare__AorB_minus_C : Not Done Yet' )
    messagebox.showinfo( 'U__compare__AorB_minus_C' , 'This function is not done yet.' )


def U__compare__AandB_minus_C() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # U__compare__AandB_minus_C : Not Done Yet' )
    messagebox.showinfo( 'U__compare__AandB_minus_C' , 'This function is not done yet.' )


def U__compare__A_and_BorC() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # U__compare__A_and_BorC : Not Done Yet' )
    messagebox.showinfo( 'U__compare__A_and_BorC' , 'This function is not done yet.' )


# endregion  # Compare Functions #######################################






###############################################################################################################
#                                                                                                             #
#                              #####  ####### #     # #     # ####### ######  #######                         #
#                             #     # #     # ##    # #     # #       #     #    #                            #
#                             #       #     # # #   # #     # #       #     #    #                            #
#                             #       #     # #  #  # #     # #####   ######     #                            #
#                             #       #     # #   # #  #   #  #       #   #      #                            #
#                             #     # #     # #    ##   # #   #       #    #     #                            #
#                              #####  ####### #     #    #    ####### #     #    #                            #
#                                                                                                             #
###############################################################################################################









########################################################################
##                            Convert Menu                            ##
########################################################################

# region     ## Convert Menu ###########################################

def menubar_convert() :

    '''Common conversion tasks'''

    pass


    ####################################################################
    ##       Convert Menu : Geo Coords: XY Decimal to Formatted       ##
    ####################################################################

    ####################################################################
    ##       Convert Menu : Geo Coords: YX Decimal to Formatted       ##
    ####################################################################

    ####################################################################
    ##       Convert Menu : Geo Coords: Formatted to XY Decimal       ##
    ####################################################################

    ####################################################################
    ##     Convert Menu : Geo Coords: Guess Format to XY Decimal      ##
    ####################################################################

    ####################################################################
    ##       Convert Menu : Unix Epoch to Formatted Timestamps        ##
    ####################################################################

    ####################################################################
    ##       Convert Menu : Formatted Timestamps to Unix Epoch        ##
    ####################################################################

    ####################################################################
    ##         Convert Menu : Guess Timestamp Format to Epoch         ##
    ####################################################################

    ####################################################################
    ##                  Convert Menu : Text Encoding                  ##
    ####################################################################

    ####################################################################
    ##                Convert Menu : ASCII Conversion                 ##
    ####################################################################

# endregion  ## Convert Menu ###########################################







###############################################################################################################
#                                                                                                             #
#                                  ####### ####### ######   #####                                             #
#                                     #    #     # #     # #     #                                            #
#                                     #    #     # #     # #                                                  #
#                                     #    #     # ######   #####                                             #
#                                     #    #     # #             #                                            #
#                                     #    #     # #       #     #                                            #
#                                     #    ####### #        #####                                             #
#                                                                                                             #
###############################################################################################################









########################################################################
##                           Text Ops Menu                            ##
########################################################################

# region     ## Text Ops Menu ##########################################

def menubar_tops() :  ## 7c4527a9e19c3febdeb5d83e775e8fc2 # 2024-10-14 17:37:25 #

    abc[  "menubar_tops"     ] = Menu( abc[  "menubar" ] , tearoff = 1 ) ; abc[  "menubar" ].add_cascade( label = "Text Ops" , menu = abc[  "menubar_tops"     ] )

    ####################################################################
    ##              Text Ops Menu : Basic Bash Commands               ##
    ####################################################################

    abc[  "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'sort (A) and unique (C)'                           , command = lambda: abc__tops__sort_unique(            "A" , "C" ) )
    abc[  "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'sort (A), unique and count (C)'                    , command = lambda: abc__tops__sort_unique_count(      "A" , "C" ) )
    abc[  "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'sort (A), unique, count and sort again (C)'        , command = lambda: abc__tops__sort_unique_count_sort( "A" , "C" ) )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Grep from (B) using args in (A) to (C)'            , command = lambda: _not_done_yet() )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Grep -i from (B) using args in (A) to (C)'         , command = lambda: _not_done_yet() )
    abc[  "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Split lines from (A) into n line groups (C)'       , command = lambda: abc__tops__split_by_n_lines( "A" , "C" ) )
    abc[  "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Shuffle lines (A) to (C)'                          , command = lambda: abc__tops__randomize_list(   "A" , "C" ) )
    abc[  "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Split (A) to Tokens (C) by Space'                  , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Split (A) to Tokens (C) with Simple Tokenizer'     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Reverse order of lines in (A) to (C)'              , command = lambda: _not_done_yet() )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Get Character Frequency in (A) to (C)'             , command = lambda: _not_done_yet() )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Group (A) by first $n Characters to (C)'           , command = lambda: _not_done_yet() )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Dedupe lines (A) by first $n Characters to (C)'    , command = lambda: _not_done_yet() )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Remove extra HTML Attributes (C) to (C)'           , command = lambda: _not_done_yet() )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Prepend (A) and Append (B) to each in (C) to (D)'  , command = lambda: _not_done_yet() )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Bulk Search and Replace from (A) to (C)'           , command = lambda: _not_done_yet() )
    #abc[ "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'Unescape Escaped Characters (A) to (C)'            , command = lambda: _not_done_yet() ) #  { "boxin" => "A" , "boxout" => "C" } )          ; } ]
    abc[  "menubar_tops" ].add_command( font = "TkFixedFont" , label = 'String Interpolate (B) using vars in (A) to to (C)' , command = lambda: abc__tops__string_interpolate( "A" , "B" , "C" ) )


    ####################################################################
    ##                Text Ops Menu : Extract Columns                 ##
    ####################################################################

    #abc[ "menubar_tops__extract_cols"     ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )

    #abc[ "menubar_tops__extract_cols"   ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )

    #abc[ "menubar_tops"  ].add_cascade( font = "TkFixedFont" , label = "Extract Columns of Text" , menu = abc[  "menubar_tops__extract_cols" ] )

    #abc[ "menubar_tops__extract_cols" ].add_command( font = "TkFixedFont" , label = 'Tab delim column in (A) to (C)'                    , command = lambda: _not_done_yet() ) # umn( { 'box' => "A" , 'sepval' => "tab"   } ) ; } ]
    #abc[ "menubar_tops__extract_cols" ].add_command( font = "TkFixedFont" , label = 'Tab delim column in (B) to (C)'                    , command = lambda: _not_done_yet() ) # umn( { 'box' => "B" , 'sepval' => "tab"   } ) ; } ]
    #abc[ "menubar_tops__extract_cols" ].add_command( font = "TkFixedFont" , label = 'Comma delim column in (A) to (C)'                  , command = lambda: _not_done_yet() ) # umn( { 'box' => "A" , 'sepval' => "comma" } ) ; } ]
    #abc[ "menubar_tops__extract_cols" ].add_command( font = "TkFixedFont" , label = 'Comma delim column in (B) to (C)'                  , command = lambda: _not_done_yet() ) # umn( { 'box' => "B" , 'sepval' => "comma" } ) ; } ]
    #abc[ "menubar_tops__extract_cols" ].add_command( font = "TkFixedFont" , label = 'Pipe delim column in (A) to (C)'                   , command = lambda: _not_done_yet() ) # umn( { 'box' => "A" , 'sepval' => "pipe"  } ) ; } ]
    #abc[ "menubar_tops__extract_cols" ].add_command( font = "TkFixedFont" , label = 'pipe delim column in (B) to (C)'                   , command = lambda: _not_done_yet() ) # umn( { 'box' => "B" , 'sepval' => "pipe"  } ) ; } ]

    ####################################################################
    ##                  Text Ops Menu : Add/Replace                   ##
    ####################################################################

    abc[  "menubar_tops__add_replace"  ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )

    abc[  "menubar_tops" ].add_cascade( font = "TkFixedFont" , label = "Add/Replace" , menu = abc[  "menubar_tops__add_replace" ] )

    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Escape Characters in (A)'                           , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "A" , "find_this" : "escape"    , "repl_with" : "newline"     } ) ) #  "\n" , "escape"  ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Add quotes to strings in (A)'                       , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "A" , "find_this" : "quote_str" , "repl_with" : "newline"     } ) ) #  "\n" , "quotes_strings"  ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Add quotes to everything in (A)'                    , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "A" , "find_this" : "quote_all" , "repl_with" : "newline"     } ) ) #  "\n" , "quotes"  ) )

    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Pipe (A) with a Newline (C)'                , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "pipe"      , "repl_with" : "newline"     } ) ) #  "|"  , "\n"      ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace white space (A) with a Newline (C)'         , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "space"     , "repl_with" : "newline"     } ) ) #  " "  , "\n"      ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace non-word chars (A) with a Newline (C)'      , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "non_word"  , "repl_with" : "newline"     } ) ) #  " "  , "\n"      ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Comma (A) with a Newline (C)'               , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "comma"     , "repl_with" : "newline"     } ) ) #  ","  , "\n"      ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace tab (A) with a Newline (C)'                 , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "tab"       , "repl_with" : "newline"     } ) ) #  "\t" , "\n"      ) )

    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with a comma (C)'               , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "comma"       } ) ) #  "\n" , ","       ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with a tab (C)'                 , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "tab"         } ) ) #  "\n" , "\t"      ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with space (C)'                 , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "space"       } ) ) #  "\n" , " "       ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with comma space (C)'           , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "comma_space" } ) ) #  "\n" , "\n\n"    ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with nothing (C)'               , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "nothing"     } ) ) #  "\n" , ""        ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with a Pipe (C)'                , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "pipe"        } ) ) #  "\n" , "|"       ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with OR (C)'                    , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "OR"          } ) ) #  "\n" , " OR "    ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with double space (C)'          , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "lflf"        } ) ) #  "\n" , "\n\n"    ) )
    abc[  "menubar_tops__add_replace" ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with a CRLF (C)'                , command = lambda: abc__tops__add_replace( **{ "fm_box" : "A" , "to_box" : "C" , "find_this" : "newline"   , "repl_with" : "crlf"        } ) ) #  "\n" , ","       ) )


    ####################################################################
    ##                Text Ops Menu : String Reversals                ##
    ####################################################################

    #abc[ "menubar_tops__newlines"         ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )

    #abc[ "menubar_tops__reverse_strings"   ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )

    #abc[ "menubar_tops"  ].add_cascade( font = "TkFixedFont" , label = "Reverse Strings and Lists" , menu = abc[  "menubar_tops__reverse_strings" ] )

    #abc[ "menubar_tops__reverse_strings"  ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )
    #abc[ "menubar_tops"  ].add_cascade( font = "TkFixedFont" , label = "String Reversal" , menu = abc[  "menubar_tops__reverse_strings" ] )

    #abc[ "menubar_tops__reverse_strings" ].add_command( font = "TkFixedFont" , label = 'Reverse String (A) to (C)'                         , command = lambda: _not_done_yet() ) #  { 'type' => 'string'                   } ) ; } ]
    #abc[ "menubar_tops__reverse_strings" ].add_command( font = "TkFixedFont" , label = 'Reverse dot Separated List (A) to (C)'             , command = lambda: _not_done_yet() ) #  { 'type' => 'list'   , "split" => '\.' , "join" => '.'  } ) ; } ]
    #abc[ "menubar_tops__reverse_strings" ].add_command( font = "TkFixedFont" , label = 'Reverse colon Separated List (A) to (C)'           , command = lambda: _not_done_yet() ) #  { 'type' => 'list'   , "split" => '\:' , "join" => ':'  } ) ; } ]
    #abc[ "menubar_tops__reverse_strings" ].add_command( font = "TkFixedFont" , label = 'Reverse pipe Separated List (A) to (C)'            , command = lambda: _not_done_yet() ) #  { 'type' => 'list'   , "split" => '\|' , "join" => '|'  } ) ; } ]
    #abc[ "menubar_tops__reverse_strings" ].add_command( font = "TkFixedFont" , label = 'Reverse comma Separated List (A) to (C)'           , command = lambda: _not_done_yet() ) #  { 'type' => 'list'   , "split" => ','  , "join" => ','  } ) ; } ]
    #abc[ "menubar_tops__reverse_strings" ].add_command( font = "TkFixedFont" , label = 'Reverse tab Separated List (A) to (C)'             , command = lambda: _not_done_yet() ) #  { 'type' => 'list'   , "split" => '\t' , "join" => "\t" } ) ; } ]
    #abc[ "menubar_tops__reverse_strings" ].add_command( font = "TkFixedFont" , label = 'Reverse semi-colon Separated List (A) to (C)'      , command = lambda: _not_done_yet() ) #  { 'type' => 'list'   , "split" => ';'  , "join" => ';'  } ) ; } ]

    ####################################################################
    ##              Text Ops Menu : More Text Splitting               ##
    ####################################################################

    #region    ## Text Ops Menu : More Text Splitting ##################

    abc[  "menubar_tops_split_more"  ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )
    abc[  "menubar_tops" ].add_cascade( font = "TkFixedFont" , label = "More Text Splitting Functions" , menu = abc[  "menubar_tops_split_more" ] )

    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace.'                                                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Dedupe.'                                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MinLen=4.'                                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MaxLen=48.'                                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. English Stops.'                                                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted.'                                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MinLen=4. Dedupe.'                                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MaxLen=48. Dedupe.'                                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. English Stops. Dedupe.'                                         , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. Dedupe.'                                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MinLen=4. MaxLen=48.'                                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MinLen=4. English Stops.'                                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MinLen=4.'                                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MaxLen=48. English Stops.'                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MaxLen=48.'                                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. English Stops.'                                         , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MinLen=4. MaxLen=48. Dedupe.'                                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MinLen=4. English Stops. Dedupe.'                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MinLen=4. Dedupe.'                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MaxLen=48. English Stops. Dedupe.'                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MaxLen=48. Dedupe.'                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. English Stops. Dedupe.'                                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MinLen=4. MaxLen=48. English Stops.'                            , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MinLen=4. MaxLen=48.'                                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MinLen=4. English Stops.'                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MaxLen=48. English Stops.'                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. MinLen=4. MaxLen=48. English Stops. Dedupe.'                    , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MinLen=4. MaxLen=48. Dedupe.'                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MinLen=4. English Stops. Dedupe.'                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MaxLen=48. English Stops. Dedupe.'                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MinLen=4. MaxLen=48. English Stops.'                    , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Whitespace. Sorted. MinLen=4. MaxLen=48. English Stops. Dedupe.'            , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "space"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer.'                                                          , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Dedupe.'                                                  , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MinLen=4.'                                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MaxLen=48.'                                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. English Stops.'                                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted.'                                                  , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MinLen=4. Dedupe.'                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MaxLen=48. Dedupe.'                                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. English Stops. Dedupe.'                                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. Dedupe.'                                          , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MinLen=4. MaxLen=48.'                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MinLen=4. English Stops.'                                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MinLen=4.'                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MaxLen=48. English Stops.'                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MaxLen=48.'                                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. English Stops.'                                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MinLen=4. MaxLen=48. Dedupe.'                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MinLen=4. English Stops. Dedupe.'                         , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MinLen=4. Dedupe.'                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MaxLen=48. English Stops. Dedupe.'                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MaxLen=48. Dedupe.'                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. English Stops. Dedupe.'                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MinLen=4. MaxLen=48. English Stops.'                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MinLen=4. MaxLen=48.'                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MinLen=4. English Stops.'                         , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MaxLen=48. English Stops.'                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. MinLen=4. MaxLen=48. English Stops. Dedupe.'              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MinLen=4. MaxLen=48. Dedupe.'                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MinLen=4. English Stops. Dedupe.'                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MaxLen=48. English Stops. Dedupe.'                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MinLen=4. MaxLen=48. English Stops.'              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Simple Tokenizer. Sorted. MinLen=4. MaxLen=48. English Stops. Dedupe.'      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "simple"   , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only.'                                                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Dedupe.'                                                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MinLen=4.'                                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MaxLen=48.'                                                    , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. English Stops.'                                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted.'                                                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MinLen=4. Dedupe.'                                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MaxLen=48. Dedupe.'                                            , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. English Stops. Dedupe.'                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. Dedupe.'                                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MinLen=4. MaxLen=48.'                                          , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MinLen=4. English Stops.'                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MinLen=4.'                                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MaxLen=48. English Stops.'                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MaxLen=48.'                                            , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. English Stops.'                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MinLen=4. MaxLen=48. Dedupe.'                                  , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MinLen=4. English Stops. Dedupe.'                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MinLen=4. Dedupe.'                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MaxLen=48. English Stops. Dedupe.'                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MaxLen=48. Dedupe.'                                    , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. English Stops. Dedupe.'                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MinLen=4. MaxLen=48. English Stops.'                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MinLen=4. MaxLen=48.'                                  , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MinLen=4. English Stops.'                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MaxLen=48. English Stops.'                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. MinLen=4. MaxLen=48. English Stops. Dedupe.'                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MinLen=4. MaxLen=48. Dedupe.'                          , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MinLen=4. English Stops. Dedupe.'                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MaxLen=48. English Stops. Dedupe.'                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MinLen=4. MaxLen=48. English Stops.'                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Alphas Only. Sorted. MinLen=4. MaxLen=48. English Stops. Dedupe.'           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "alpha"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars'                                                                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Dedupe.'                                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MinLen=4.'                                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MaxLen=48.'                                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. English Stops.'                                                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted.'                                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MinLen=4. Dedupe.'                                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MaxLen=48. Dedupe.'                                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. English Stops. Dedupe.'                                         , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. Dedupe.'                                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MinLen=4. MaxLen=48.'                                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MinLen=4. English Stops.'                                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MinLen=4.'                                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MaxLen=48. English Stops.'                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MaxLen=48.'                                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. English Stops.'                                         , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MinLen=4. MaxLen=48. Dedupe.'                                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MinLen=4. English Stops. Dedupe.'                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MinLen=4. Dedupe.'                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MaxLen=48. English Stops. Dedupe.'                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MaxLen=48. Dedupe.'                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. English Stops. Dedupe.'                                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MinLen=4. MaxLen=48. English Stops.'                            , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MinLen=4. MaxLen=48.'                                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MinLen=4. English Stops.'                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MaxLen=48. English Stops.'                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. MinLen=4. MaxLen=48. English Stops. Dedupe.'                    , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MinLen=4. MaxLen=48. Dedupe.'                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MinLen=4. English Stops. Dedupe.'                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MaxLen=48. English Stops. Dedupe.'                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MinLen=4. MaxLen=48. English Stops.'                    , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Word Chars. Sorted. MinLen=4. MaxLen=48. English Stops. Dedupe.'            , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "words"    , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
   
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer.'                                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Dedupe.'                                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MinLen=4.'                                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MaxLen=48.'                                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. English Stops.'                                         , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted.'                                                , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MinLen=4. Dedupe.'                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MaxLen=48. Dedupe.'                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. English Stops. Dedupe.'                                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. Dedupe.'                                        , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MinLen=4. MaxLen=48.'                                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MinLen=4. English Stops.'                               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MinLen=4.'                                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MaxLen=48. English Stops.'                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MaxLen=48.'                                     , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. English Stops.'                                 , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MinLen=4. MaxLen=48. Dedupe.'                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MinLen=4. English Stops. Dedupe.'                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MinLen=4. Dedupe.'                              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MaxLen=48. English Stops. Dedupe.'                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MaxLen=48. Dedupe.'                             , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. English Stops. Dedupe.'                         , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MinLen=4. MaxLen=48. English Stops.'                    , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MinLen=4. MaxLen=48.'                           , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MinLen=4. English Stops.'                       , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MaxLen=48. English Stops.'                      , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. MinLen=4. MaxLen=48. English Stops. Dedupe.'            , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 0 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MinLen=4. MaxLen=48. Dedupe.'                   , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 0 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MinLen=4. English Stops. Dedupe.'               , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" :  0 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MaxLen=48. English Stops. Dedupe.'              , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 0 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    #abc[ "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MinLen=4. MaxLen=48. English Stops.'            , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 0 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )
    abc[  "menubar_tops_split_more" ].add_command( font = "TkFixedFont" , label = 'Standard Tokenizer. Sorted. MinLen=4. MaxLen=48. English Stops. Dedupe.'    , command = lambda: abc__tops__split_string_by( **{ "fm_box" : "A" , "to_box" : "C" , "split_by" : "standard" , "dedupe" : 1 , "min_token_length" : 4 , "max_token_length" : 48 , "en_stops" : 1 , "sort_it" : 1 } ) )

    #endregion ## Text Ops Menu : More Text Splitting ##################


    ####################################################################
    ##                    Text Ops Menu : Examples                    ##
    ####################################################################

    ####################################################################

    abc[  "menubar_tops" ].add_separator()

    ####################################################################

    abc[  "menubar_tops__examples" ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )

    abc[  "menubar_tops" ].add_cascade( font = "TkFixedFont" , label = "Text Ops Examples" , menu = abc[  "menubar_tops__examples" ] )

    abc[  "menubar_tops__examples" ].add_command( font = "TkFixedFont" , label = 'String Interpolate : Ping'            , command = lambda: abc__tops__examples( "abc__tops__interpolate_ping" ) )
    abc[  "menubar_tops__examples" ].add_command( font = "TkFixedFont" , label = 'String Interpolate : Ping with status', command = lambda: abc__tops__examples( "abc__tops__interpolate_ping_status" ) )
    abc[  "menubar_tops__examples" ].add_command( font = "TkFixedFont" , label = 'String Interpolate : Ping with color' , command = lambda: abc__tops__examples( "abc__tops__interpolate_ping_color" ) )
    abc[  "menubar_tops__examples" ].add_command( font = "TkFixedFont" , label = 'String Interpolate : NMap Advanced'   , command = lambda: abc__tops__examples( "abc__tops__interpolate_nmap_advanced" ) )


    ####################################################################

    abc[  "menubar_tops" ].add_separator()

    ####################################################################

    abc[  "menubar_tops__help" ] = Menu( abc[  "menubar_tops" ] , tearoff = 1 )

    abc[  "menubar_tops" ].add_cascade( font = "TkFixedFont" , label = "Help with Text Ops functions" , menu = abc[  "menubar_tops__help" ] )

    abc[  "menubar_tops__help" ].add_command( font = "TkFixedFont" , label = 'Help : sort (A) and unique (C)' , command = lambda: abc__tops__help( "abc__tops__sort_unique" ) )

# endregion  ## Text Ops Menu ##########################################











########################################################################
##                         Text Ops Functions                         ##
########################################################################

# region     # Text Ops Functions ######################################



def abc__tops__add_replace( **kwargs ) :  ## f627f3ca194584fe35e9c914e6557ed2 # 2024-10-14 11:35:14 #

    fm_box    = kwargs.get( "fm_box"    , "A" )
    to_box    = kwargs.get( "to_box"    , "C" )

    find_this = { 
            "newline"   : r"\n" 
        ,   "crnl"      : r"\r\n" 
        ,   "non_word"  : r"\W+" 
        ,   "non_space" : r"\S+" 
        ,   "space"     : r"\s+" 
        ,   "comma"     : r"," 
        ,   "tab"       : r"\t" 
        ,   "pipe"      : r"|" 
        }.get( kwargs.get( "find_this" ) , "space" )

    repl_with = { 
            "newline"     :  "\n" 
        ,   "comma"       : r"," 
        ,   "tab"         :  "\t" 
        ,   "space"       : r"  " 
        ,   "comma_space" : r", " 
        ,   "nothing"     : r"" 
        ,   "pipe"        : r"|" 
        ,   "OR"          : r" OR " 
        ,   "lflf"        :  "\n\n" 
        ,   "crlf"        :  "\r\n" 
        }.get( kwargs.get( "repl_with" ) , "nl" )

    timenow = datetime.datetime.now()

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__tops__add_replace( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" , "find_this" : "{repr(find_this)}" , "repl_with" : "{repr(repl_with)}" }} )' )

    if   find_this == "crnl" : pass
    elif find_this == "nl" : pass
    else :

        lst_to = []

        for x in [ x for x in re.split( find_this , box[ fm_box ].get( "1.0" , 'end-1c' ) ) if x and x.strip() ] : lst_to.append( x )

        if lst_to : 
            
            _clear_box( to_box )
            
            box[ to_box ].insert( "end" , f'{repl_with.join(lst_to)}\n' )


def abc__tops__randomize_list( fm_box , to_box ) :  ## 80293db13c24fb70f816073cb8b6b81a # 2024-04-10 10:20:06 #

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

    random.shuffle(lst_fm)

    _clear_box( to_box )

    for x in lst_fm :

        box[ to_box ].insert( "end" , f'{x}\n' )


def abc__tops__sort_unique( fm_box , to_box ) :

    fm_set = set( box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() )

    _clear_box( to_box )

    for x in sorted( fm_set ) :

        box[ to_box ].insert( "end" , f'{x}\n' )


def abc__tops__sort_unique_count( fm_box , to_box ) :

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

    cnt_fm = Counter( lst_fm )

    _clear_box( to_box )

    for v , c in sorted( cnt_fm.items() ) :

        box[ to_box ].insert( "end" , f'{c:8,d} : {v}\n' )


def abc__tops__sort_unique_count_sort( fm_box , to_box ) :

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

    cnt_fm = Counter( lst_fm )

    _clear_box( to_box )

    for v , c in cnt_fm.most_common() :

        box[ to_box ].insert( "end" , f'{c:8,d} : {v}\n' )


def abc__tops__string_interpolate( vars_box , str_box , to_box ) :  ## 8c30bbab6c1a3ba7dc86f3139fa5633f # 2024-10-14 17:39:32 #

  lst_vars  = [ x.strip() for x in box[ vars_box ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ]
  repl_old = box[ str_box ].get( "1.0" , 'end-1c' )

  search_vars = {}

  _clear_box( to_box )

  for var in lst_vars :

    if not var.strip() : continue

    if kv := re.search( r'^(\S+)\s?=\s?(..*)$' , var ) :
      search_vars |= { kv.groups(1) , kv.groups(2) }
    else :
      repl_new = repl_old
      for k,v in search_vars.items() : repl_new = repl_new.replace( f'#{{{k}}}' , v )
      repl_new = repl_new.replace( r'#{ReplaceMe}' , var ) # default string to replace
      box[ to_box ].insert( "end" , f'{repl_new}\n' )


def abc__tops__split_string_by( **kwargs ) :  ## 621901c9724e1436983db3f8f0908171 # 2024-10-14 01:04:34 #

    timenow = datetime.datetime.now()

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )
    split_by  = kwargs.get( "split_by"  , "space" )
    dedupe    = kwargs.get( "dedupe"    , 0       )
    sort_it   = kwargs.get( "sort_it"   , 0       )

    stops_en         = kwargs.get( "stops_en"         , 0 )
    min_token_length = kwargs.get( "min_token_length" , 0 )
    max_token_length = kwargs.get( "max_token_length" , 0 )

    english_stops=[ "a","an","and","are","as","at","be","but","by","for","if","in","into","is","it","no","not","of","on","or","such","that","the","their","then","there","these","they","this","to","was","will","with" ]
    # english_stop_long_list=[ "'ll","'tis","'twas","'ve","10","39","a","a's","able","ableabout","about","above","abroad","abst","accordance","according","accordingly","across","act","actually","ad","added","adj","adopted","ae","af","affected","affecting","affects","after","afterwards","ag","again","against","ago","ah","ahead","ai","ain't","aint","al","all","allow","allows","almost","alone","along","alongside","already","also","although","always","am","amid","amidst","among","amongst","amoungst","amount","an","and","announce","another","any","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","ao","apart","apparently","appear","appreciate","appropriate","approximately","aq","ar","are","area","areas","aren","aren't","arent","arise","around","arpa","as","aside","ask","asked","asking","asks","associated","at","au","auth","available","aw","away","awfully","az","b","ba","back","backed","backing","backs","backward","backwards","bb","bd","be","became","because","become","becomes","becoming","been","before","beforehand","began","begin","beginning","beginnings","begins","behind","being","beings","believe","below","beside","besides","best","better","between","beyond","bf","bg","bh","bi","big","bill","billion","biol","bj","bm","bn","bo","both","bottom","br","brief","briefly","bs","bt","but","buy","bv","bw","by","bz","c","c'mon","c's","ca","call","came","can","can't","cannot","cant","caption","case","cases","cause","causes","cc","cd","certain","certainly","cf","cg","ch","changes","ci","ck","cl","clear","clearly","click","cm","cmon","cn","co","co.","com","come","comes","computer","con","concerning","consequently","consider","considering","contain","containing","contains","copy","corresponding","could","could've","couldn","couldn't","couldnt","course","cr","cry","cs","cu","currently","cv","cx","cy","cz","d","dare","daren't","darent","date","de","dear","definitely","describe","described","despite","detail","did","didn","didn't","didnt","differ","different","differently","directly","dj","dk","dm","do","does","doesn","doesn't","doesnt","doing","don","don't","done","dont","doubtful","down","downed","downing","downs","downwards","due","during","dz","e","each","early","ec","ed","edu","ee","effect","eg","eh","eight","eighty","either","eleven","else","elsewhere","empty","end","ended","ending","ends","enough","entirely","er","es","especially","et","et-al","etc","even","evenly","ever","evermore","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","face","faces","fact","facts","fairly","far","farther","felt","few","fewer","ff","fi","fifteen","fifth","fifty","fify","fill","find","finds","fire","first","five","fix","fj","fk","fm","fo","followed","following","follows","for","forever","former","formerly","forth","forty","forward","found","four","fr","free","from","front","full","fully","further","furthered","furthering","furthermore","furthers","fx","g","ga","gave","gb","gd","ge","general","generally","get","gets","getting","gf","gg","gh","gi","give","given","gives","giving","gl","gm","gmt","gn","go","goes","going","gone","good","goods","got","gotten","gov","gp","gq","gr","great","greater","greatest","greetings","group","grouped","grouping","groups","gs","gt","gu","gw","gy","h","had","hadn't","hadnt","half","happens","hardly","has","hasn","hasn't","hasnt","have","haven","haven't","havent","having","he","he'd","he'll","he's","hed","hell","hello","help","hence","her","here","here's","hereafter","hereby","herein","heres","hereupon","hers","herself","herse”","hes","hi","hid","high","higher","highest","him","himself","himse”","his","hither","hk","hm","hn","home","homepage","hopefully","how","how'd","how'll","how's","howbeit","however","hr","ht","htm","html","http","hu","hundred","i","i'd","i'll","i'm","i've","i.e.","id","ie","if","ignored","ii","il","ill","im","immediate","immediately","importance","important","in","inasmuch","inc","inc.","indeed","index","indicate","indicated","indicates","information","inner","inside","insofar","instead","int","interest","interested","interesting","interests","into","invention","inward","io","iq","ir","is","isn","isn't","isnt","it","it'd","it'll","it's","itd","itll","its","itself","itse”","ive","j","je","jm","jo","join","jp","just","k","ke","keep","keeps","kept","keys","kg","kh","ki","kind","km","kn","knew","know","known","knows","kp","kr","kw","ky","kz","l","la","large","largely","last","lately","later","latest","latter","latterly","lb","lc","least","length","less","lest","let","let's","lets","li","like","liked","likely","likewise","line","little","lk","ll","long","longer","longest","look","looking","looks","low","lower","lr","ls","lt","ltd","lu","lv","ly","m","ma","made","mainly","make","makes","making","man","many","may","maybe","mayn't","maynt","mc","md","me","mean","means","meantime","meanwhile","member","members","men","merely","mg","mh","microsoft","might","might've","mightn't","mightnt","mil","mill","million","mine","minus","miss","mk","ml","mm","mn","mo","more","moreover","most","mostly","move","mp","mq","mr","mrs","ms","msie","mt","mu","much","mug","must","must've","mustn't","mustnt","mv","mw","mx","my","myself","myse”","mz","n","na","name","namely","nay","nc","nd","ne","near","nearly","necessarily","necessary","need","needed","needing","needn't","neednt","needs","neither","net","netscape","never","neverf","neverless","nevertheless","new","newer","newest","next","nf","ng","ni","nine","ninety","nl","no","no-one","nobody","non","none","nonetheless","noone","nor","normally","nos","not","noted","nothing","notwithstanding","novel","now","nowhere","np","nr","nu","null","number","numbers","nz","o","obtain","obtained","obviously","of","off","often","oh","ok","okay","old","older","oldest","om","omitted","on","once","one","one's","ones","only","onto","open","opened","opening","opens","opposite","or","ord","order","ordered","ordering","orders","org","other","others","otherwise","ought","oughtn't","oughtnt","our","ours","ourselves","out","outside","over","overall","owing","own","p","pa","page","pages","part","parted","particular","particularly","parting","parts","past","pe","per","perhaps","pf","pg","ph","pk","pl","place","placed","places","please","plus","pm","pmid","pn","point","pointed","pointing","points","poorly","possible","possibly","potentially","pp","pr","predominantly","present","presented","presenting","presents","presumably","previously","primarily","probably","problem","problems","promptly","proud","provided","provides","pt","put","puts","pw","py","q","qa","que","quickly","quite","qv","r","ran","rather","rd","re","readily","really","reasonably","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","reserved","respectively","resulted","resulting","results","right","ring","ro","room","rooms","round","ru","run","rw","s","sa","said","same","saw","say","saying","says","sb","sc","sd","se","sec","second","secondly","seconds","section","see","seeing","seem","seemed","seeming","seems","seen","sees","self","selves","sensible","sent","serious","seriously","seven","seventy","several","sg","sh","shall","shan't","shant","she","she'd","she'll","she's","shed","shell","shes","should","should've","shouldn","shouldn't","shouldnt","show","showed","showing","shown","showns","shows","si","side","sides","significant","significantly","similar","similarly","since","sincere","site","six","sixty","sj","sk","sl","slightly","sm","small","smaller","smallest","sn","so","some","somebody","someday","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","sr","st","state","states","still","stop","strongly","su","sub","substantially","successfully","such","sufficiently","suggest","sup","sure","sv","sy","system","sz","t","t's","take","taken","taking","tc","td","tell","ten","tends","test","text","tf","tg","th","than","thank","thanks","thanx","that","that'll","that's","that've","thatll","thats","thatve","the","their","theirs","them","themselves","then","thence","there","there'd","there'll","there're","there's","there've","thereafter","thereby","thered","therefore","therein","therell","thereof","therere","theres","thereto","thereupon","thereve","these","they","they'd","they'll","they're","they've","theyd","theyll","theyre","theyve","thick","thin","thing","things","think","thinks","third","thirty","this","thorough","thoroughly","those","thou","though","thoughh","thought","thoughts","thousand","three","throug","through","throughout","thru","thus","til","till","tip","tis","tj","tk","tm","tn","to","today","together","too","took","top","toward","towards","tp","tr","tried","tries","trillion","truly","try","trying","ts","tt","turn","turned","turning","turns","tv","tw","twas","twelve","twenty","twice","two","tz","u","ua","ug","uk","um","un","under","underneath","undoing","unfortunately","unless","unlike","unlikely","until","unto","up","upon","ups","upwards","us","use","used","useful","usefully","usefulness","uses","using","usually","uucp","uy","uz","v","va","value","various","vc","ve","versus","very","vg","vi","via","viz","vn","vol","vols","vs","vu","w","want","wanted","wanting","wants","was","wasn","wasn't","wasnt","way","ways","we","we'd","we'll","we're","we've","web","webpage","website","wed","welcome","well","wells","went","were","weren","weren't","werent","weve","wf","what","what'd","what'll","what's","what've","whatever","whatll","whats","whatve","when","when'd","when'll","when's","whence","whenever","where","where'd","where'll","where's","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","which","whichever","while","whilst","whim","whither","who","who'd","who'll","who's","whod","whoever","whole","wholl","whom","whomever","whos","whose","why","why'd","why'll","why's","widely","width","will","willing","wish","with","within","without","won","won't","wonder","wont","words","work","worked","working","works","world","would","would've","wouldn","wouldn't","wouldnt","ws","www","x","y","ye","year","years","yes","yet","you","you'd","you'll","you're","you've","youd","youll","young","younger","youngest","your","youre","yours","yourself","yourselves","youve","yt","yu","z","za","zero","zm","zr" ]

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} #' , f'{getframeinfo(currentframe()).lineno:4,d}' , f' # abc__tops__split_string_by( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}"  , "split_by"  : "{split_by}" , "dedupe" : {dedupe} }} )' )

    str_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).strip()

    tokens = []

    if   split_by == "space"    : tokens = [ x            for x in str_fm.split()                                         if x and str(x).strip() ]
    elif split_by == "simple"   : tokens = [ x.casefold() for x in re.findall( r'[a-zA-Z0-9@.-]+' , str_fm )              if x and str(x).strip() ] 
    elif split_by == "alpha"    : tokens = [ x            for x in re.findall( r'[a-z]+'          , str_fm )              if x and str(x).strip() ] 
    elif split_by == "words"    : tokens = [ x            for x in re.findall( r'\w+'             , str_fm )              if x and str(x).strip() ] 
    elif split_by == "standard" : tokens = [ x.casefold() for x in re.findall (r'\w+|[^\w\s]'     , str_fm , re.UNICODE ) if x and str(x).strip() ] 

    if dedupe           : tokens = list( set( tokens ) )
    if min_token_length : tokens = [ token for token in tokens if len( token ) >= min_token_length ]
    if max_token_length : tokens = [ token for token in tokens if len( token ) <= max_token_length ]
    if stops_en         : tokens = [ token for token in tokens if token.casefold() not in english_stops ]
    if sort_it          : tokens = sorted( tokens , key=str.casefold )

    if tokens : 
        _clear_box( to_box )
        for x in tokens : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__tops__split_by_n_lines( fm_box , to_box ) :  ## 3de32b95b63ad1d50c6fb9abe185102d # 2024-10-14 17:45:03 #

    timenow = datetime.datetime.now()

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__tops__split_by_n_lines( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    there_is_no_window = True

    def _do_this_function( split_by ) :

        try     : split_by_int = int(split_by.get())
        except  : split_by_int = None

        print( f'# INFO # {"abc__tops__split_by_n_lines":48} # fm_box : {fm_box} | to_box : {to_box} | split_by_int : {split_by_int}')

        if not isinstance( split_by_int, int ) :
            messagebox.showinfo( 'Doh!.' , 'Entry Must be an integer.' )
            return

        lst_fm = [ x for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() if x and x.strip() ]

        _clear_box( to_box )

        for i , v in enumerate( lst_fm , start=1 ) :

            box[ to_box ].insert( "end" , f'{v}\n' )

            if i % split_by_int == 0 : box[ to_box ].insert( "end" , abc[  "options_record_separator" ].get() )

    if there_is_no_window :

        entry_box = {}
        entry_box[ "Toplevel" ] = Toplevel()

        entry_box[ "Toplevel" ].title( "Enter Arguments" )

        entry_box[ "ArgsFrame1"  ] = Frame( entry_box[ "Toplevel" ] , relief = 'flat' , borderwidth = 0 ) ; entry_box[ "ArgsFrame1"  ].pack( side = "top"  , fill = "x" , expand = "yes" )
        
        entry_box[ "q1" ] = Label( entry_box[ "ArgsFrame1" ] , text = "Split By This Many Lines : " )     ; entry_box[ "q1"          ].pack( side = "left" , fill = "x" , expand = "yes" )
        entry_box[ "a1" ] = Entry( entry_box[ "ArgsFrame1" ]                                        )     ; entry_box[ "a1"          ].pack( side = "left" , fill = "x" , expand = "yes" )

        entry_box[ "ButtonFrame"  ] = Frame(  entry_box[ "Toplevel"    ] , relief = 'flat'   , borderwidth = 0 )                                          ; entry_box[ "ButtonFrame"  ].pack( side = "top"  , fill = "x" , expand = "yes" )
        entry_box[ "Button_Close" ] = Button( entry_box[ "ButtonFrame" ] , text='Close'      , command = entry_box[ "Toplevel" ].destroy                ) ; entry_box[ "Button_Close" ].pack( side = "left" , fill = "x" , expand = "yes" )
        entry_box[ "Button_Apply" ] = Button( entry_box[ "ButtonFrame" ] , text='Make it so' , command = lambda: _do_this_function( entry_box[ "a1" ] ) ) ; entry_box[ "Button_Apply" ].pack( side = "left" , fill = "x" , expand = "yes" )


def abc__tops__sort_lines( **kwargs ) :  ## d4a39a19110ee0f3c732a85430bf63e7 # 2024-10-14 16:42:22 #

    timenow = datetime.datetime.now()

    fm_box     = kwargs.get( "fm_box"     , "A"     )
    to_box     = kwargs.get( "to_box"     , fm_box  )
    sort_what  = kwargs.get( "sort_what"  , "lines" )
    sort_order = kwargs.get( "sort_order" , "AZ"    )
    sort_case  = kwargs.get( "sort_case"  , 0       )
    print_head = kwargs.get( "print_head" , 0       )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # _sort_lines( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}"  , "sort_what"  : {sort_what} , "sort_order" : {sort_order} , "sort_case"  : {sort_case} }} )' )

    lst_fm = [ x for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() if x and str(x).strip() and r'## Succesfully Parsed ##' not in x and r'## Failed To Parse ##' not in x ]

    _clear_box( to_box )
    
    sorted_lines = []
    failed_lines = []

    if   sort_what == "lines"  :

        if   sort_order == "AZ"   and sort_case : sorted_lines = sorted( lst_fm                                   )
        elif sort_order == "AZ"                 : sorted_lines = sorted( lst_fm , key=str.casefold                )
        elif sort_order == "ZA"   and sort_case : sorted_lines = sorted( lst_fm                    , reverse=True )
        elif sort_order == "ZA"                 : sorted_lines = sorted( lst_fm , key=str.casefold , reverse=True )

        elif sort_order == "SLAZ" and sort_case : sorted_lines = sorted( lst_fm , key=lambda x: (  len( x ) , x            )                 )
        elif sort_order == "SLAZ"               : sorted_lines = sorted( lst_fm , key=lambda x: (  len( x ) , x.casefold() )                 )
        elif sort_order == "SLZA" and sort_case : sorted_lines = sorted( lst_fm , key=lambda x: ( -len( x ) , x            ) , reverse=True  )
        elif sort_order == "SLZA"               : sorted_lines = sorted( lst_fm , key=lambda x: ( -len( x ) , x.casefold() ) , reverse=True  )

        elif sort_order == "LSAZ" and sort_case : sorted_lines = sorted( lst_fm , key=lambda x: ( -len( x ) , x            )                 )
        elif sort_order == "LSAZ"               : sorted_lines = sorted( lst_fm , key=lambda x: ( -len( x ) , x.casefold() )                 )
        elif sort_order == "LSZA" and sort_case : sorted_lines = sorted( lst_fm , key=lambda x: (  len( x ) , x            ) , reverse=True  )
        elif sort_order == "LSZA"               : sorted_lines = sorted( lst_fm , key=lambda x: (  len( x ) , x.casefold() ) , reverse=True  )

    elif sort_what == "ipaddr" :

        for x in lst_fm :
        
            if '.' not in x : failed_lines.append( x ) ; continue  ## IPs have dots. if not, Fail
            
            try :
                y = tuple( map( int , x.split( '.' ) ) )
                if len( y ) != 4 : failed_lines.append( x ) ; continue  ## IPs have 4 octects. If not, Fail
            except : failed_lines.append( x ) ; continue

            if not all( 0 <= num <= 255 for num in y ) : failed_lines.append( x ) ; continue ## IPs have 4 octects between 0 and 255. If not, Fail

            sorted_lines.append( x )

        if   sort_order == "AZ" : sorted_lines = sorted( sorted_lines , key=lambda ip: tuple( map( int , ip.split( '.' ) ) )                )
        elif sort_order == "ZA" : sorted_lines = sorted( sorted_lines , key=lambda ip: tuple( map( int , ip.split( '.' ) ) ) , reverse=True )

    elif sort_what == "domain" :

        ## Reverse Strings #############################################
        
        reverse_lines = []

        for x in lst_fm :
        
            if '.' not in x : failed_lines.append( x ) ; continue
            reverse_lines.append( '.'.join( x.split('.')[::-1] ) )

        ## Sort It #####################################################

        if   sort_order == "AZ" and sort_case is False : reverse_lines = sorted( [ x for x in reverse_lines if x ] , key=str.casefold                )
        elif sort_order == "ZA" and sort_case is False : reverse_lines = sorted( [ x for x in reverse_lines if x ] , key=str.casefold , reverse=True )

        ## Put it back #################################################

        for x in reverse_lines : sorted_lines.append( '.'.join( x.split('.')[::-1] ) )

    elif sort_what == "email"  :
        
        reverse_lines = []

        ## Reverse Strings #############################################
        ## Rearrange admin@mail.yahoo.com to com.yahoo.mail@admin 

        for x in lst_fm :

            if '@' not in x : failed_lines.append( x ) ; continue
            if '.' not in x : failed_lines.append( x ) ; continue

            username_domain = x.split('@')
            if len( username_domain ) != 2 : failed_lines.append( x ) ; continue

            username , domain = username_domain
            reversed_domain = '.'.join(domain.split('.')[::-1])

            reverse_lines.append( f'{reversed_domain}@{username}' )

        if   sort_order == "AZ" : reverse_lines = sorted( [ x for x in reverse_lines if x ] , key=str.casefold                )
        elif sort_order == "ZA" : reverse_lines = sorted( [ x for x in reverse_lines if x ] , key=str.casefold , reverse=True )

        ## Put it back #################################################

        for x in [ x for x in reverse_lines if x ] :

            domain , username = x.split('@')
            domain = '.'.join(domain.split('.')[::-1])

            sorted_lines.append( f'{username}@{domain}' )
    
    ## Send back to the Box ############################################

    if failed_lines :

        if print_head : box[ to_box ].insert( "end" , "## Failed To Parse #############################\n\n" )
        for x in failed_lines : box[ to_box ].insert( "end" , f"{x}\n" )
        if sorted_lines : print()

    if sorted_lines :

        if print_head : box[ to_box ].insert( "end" , "## Succesfully Parsed ##########################\n\n" )
        for x in sorted_lines : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__tops__examples( help_with ) :  ## f31f951ef4dd2dd7747841beceab68b8 # 2024-04-10 10:19:09 #

    if help_with == "abc__tops__interpolate_ping" :

        _clear_box( "A" )
        _clear_box( "B" )

        box[ "A" ].insert( "end" , 
            "\n".join( [
                  r'''192.168.1.3'''
                , r'''192.168.1.4'''
                , r'''192.168.1.5'''
            ] ) )

        box[ "B" ].insert( "end" , r'''ping -c2 #{ReplaceMe}''' )

        message_text  = "This creates a pastable list of ping commands using the IPs listed in Box A\n\nClick on the Text Ops : String Interpolate menu item to execute this function using this data."

        messagebox.showinfo( 'Text Ops : String Interpolate. Ping' , message_text )

    elif help_with == "abc__tops__interpolate_ping_status" :

        _clear_box( "A" )
        _clear_box( "B" )

        box[ "A" ].insert( "end" , 
            "\n".join( [
                  r'''192.168.1.3'''
                , r'''192.168.1.4'''
                , r'''192.168.1.5'''
            ] ) )

        box[ "B" ].insert( "end" , r'''ping -c2 #{ReplaceMe} > /dev/null && printf "# Good : #{ReplaceMe}\n" || printf "# Bad  : #{ReplaceMe}\n"''' )

        message_text  = "This creates a pastable list of ping commands using the IPs listed in Box A. This command only shows the status of the ping and not the typical output.\n\nClick on the Text Ops : String Interpolate menu item to execute this function using this data."

        messagebox.showinfo( 'Text Ops : String Interpolate. Ping status' , message_text )

    elif help_with == "abc__tops__interpolate_ping_color" :

        _clear_box( "A" )
        _clear_box( "B" )

        box[ "A" ].insert( "end" , 
            "\n".join( [
                  r'''192.168.1.3'''
                , r'''192.168.1.4'''
                , r'''192.168.1.5'''
            ] ) )

        box[ "B" ].insert( "end" , r'''ping -c2 #{ReplaceMe} > /dev/null && printf "# %-15s : \e[0;32m%s\e[0m\n" #{ReplaceMe} "Ping Good" || printf "# %-15s : \e[0;31m%s\e[0m\n" #{ReplaceMe} "Ping Bad" &''' )

        message_text  = "This creates a pastable list of ping commands using the IPs listed in Box A. This command shows a color coded status of the ping results.\n\nClick on the Text Ops : String Interpolate menu item to execute this function using this data."

        messagebox.showinfo( 'Text Ops : String Interpolate. Ping with Flair' , message_text )

    elif help_with == "abc__tops__interpolate_nmap_advanced" :

        _clear_box( "A" )
        _clear_box( "B" )

        box[ "A" ].insert( "end" , 
            "\n".join( [
                  r'''RIGHT_NOW = `date +%Y_%m%d_%H%M%S`'''
                , r'''PROJECT_NAME = TESTPROJECT'''
                , r'''SCAN_DIR = ~/share/data/scans'''
                , r''''''
                , r'''NMAP_FLAG1 = -Pn -n'''
                , r'''NMAP_FLAG2 = '''
                , r'''NMAP_SCAN_NAME = discover'''
                , r'''192.168.1.3'''
                , r'''192.168.1.4'''
                , r'''192.168.1.5'''
                , r''''''
                , r'''NMAP_FLAG1 = -Pn -n -sS -p-'''
                , r'''NMAP_FLAG2 = -vvv --open'''
                , r'''NMAP_SCAN_NAME = fullScan'''
                , r'''192.168.1.3'''
                , r'''192.168.1.4'''
                , r'''192.168.1.5'''
            ] ) )

        box[ "B" ].insert( "end" , 
            "\n".join( [
                  r'''## Auto Generated. Do not edit''' 
                , r'''RIGHT_NOW=#{RIGHT_NOW}''' 
                , r'''sudo nmap #{NMAP_FLAG1} #{NMAP_FLAG2} -oA #{SCAN_DIR}/#{PROJECT_NAME}-#{NMAP_SCAN_NAME}-${RIGHT_NOW} #{ReplaceMe}''' 
                , r'''''' 
                , r'''cat #{SCAN_DIR}/#{PROJECT_NAME}-#{NMAP_SCAN_NAME}-${RIGHT_NOW}.gnmap | perl -ne 'if(/Host: (\d\S+)\s.*?\tPorts: (..*?)\t/){($ip,$p)=($1,$2);@P;for my $x(split(/\s*,\s*/,$p)){next unless($x=~/\/open\//);($x=$x)=~s/^(\d+)\/.*$/\1/;push(@P,$x)}printf("time nmap -sC -oA default_scripts -v -p %s %s\n",join(",",@P),$ip)}' ''' 
                , r'''''' 
            ] ) )

        message_text  = "This sets and re-sets the variables associated with NMAP and then applies those to each of the IP addresses.\n\nClick on the Text Ops : String Interpolate menu item to execute this function using this data."

        messagebox.showinfo( 'Text Ops : String Interpolate. NMap Advanced' , message_text )


def abc__tops__help( help_with ) :  ## d71b195f81e23a3961b942b13e84671a # 2024-04-10 10:19:27 #

    if help_with == "abc__tops__sort_unique" :

        message_text  = "This will sort and deduplicate all lines in Box A and print the results in Box C"

        messagebox.showinfo( 'Text Ops : sort and unique' , message_text )



def abc__tops__multiple_grep() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__tops__multiple_grep : Not Done Yet' )
    messagebox.showinfo( 'abc__tops__multiple_grep' , 'This function is not done yet.' )

def abc__tops__bulk_replace() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__tops__bulk_replace : Not Done Yet' )
    messagebox.showinfo( 'abc__tops__bulk_replace' , 'This function is not done yet.' )

def abc__tops__extract_columns() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__tops__extract_columns : Not Done Yet' )
    messagebox.showinfo( 'abc__tops__extract_columns' , 'This function is not done yet.' )

def abc__tops__reverse_strings() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__tops__reverse_strings : Not Done Yet' )
    messagebox.showinfo( 'abc__tops__reverse_strings' , 'This function is not done yet.' )

def abc__tops__group_by_first_chars() : 
    timenow = datetime.datetime.now()
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__tops__group_by_first_chars : Not Done Yet' )
    messagebox.showinfo( 'abc__tops__group_by_first_chars' , 'This function is not done yet.' )




# endregion  # Text Ops Functions ######################################







###########################################################################################################
#                                                                                                         #
#                                 ####### ####### ######   #####                                          #
#                                 #       #     # #     # #     #                                         #
#                                 #       #     # #     # #                                               #
#                                 #####   #     # ######   #####                                          #
#                                 #       #     # #             #                                         #
#                                 #       #     # #       #     #                                         #
#                                 #       ####### #        #####                                          #
#                                                                                                         #
###########################################################################################################


########################################################################
##                           File Ops Menu                            ##
########################################################################

# region     ## File Ops Menu ##########################################

def menubar_fops() :

    '''Common file tasks'''

    pass


    #abc[ "menubar_fops" ] = Menu( abc[  "menubar" ] , tearoff = 1 ) ; abc[  "menubar" ].add_cascade( label = "File Ops"  , menu = abc[  "menubar_fops" ] )

    ####################################################################

    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Find Duplicate Files in Single Directory'         , command = lambda: _not_done_yet() )
    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Find Duplicate Files Multi-Select'                , command = lambda: _not_done_yet() )
    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Find Duplicate Files Recursively'                 , command = lambda: _not_done_yet() )
    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Find Duplicate Files in Single Directory (>1MiB)' , command = lambda: _not_done_yet() )
    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Find Duplicate Files Multi-Select (>1MiB)'        , command = lambda: _not_done_yet() )
    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Find Duplicate Files Recursively (>1MiB)'         , command = lambda: _not_done_yet() )
    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Hash Files in Single Directory MD5'               , command = lambda: _not_done_yet() )
    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Hash Files Multi-Select MD5'                      , command = lambda: _not_done_yet() )
    #abc[ "menubar_fops" ].add_command( font = "TkFixedFont" , label = 'Hash Files Recursively MD5'                       , command = lambda: _not_done_yet() )


# endregion  ## File Ops Menu ##########################################






###############################################################################################################
#                                                                                                             #
#                                      #####  ####### ######  #######                                         #
#                                     #     # #     # #     # #                                               #
#                                     #       #     # #     # #                                               #
#                                     #       #     # #     # #####                                           #
#                                     #       #     # #     # #                                               #
#                                     #     # #     # #     # #                                               #
#                                      #####  ####### ######  #######                                         #
#                                                                                                             #
###############################################################################################################









########################################################################
##                             Code Menu                              ##
########################################################################

# region     ## Code Menu ##############################################

def menubar_code() :  ## 532822d83797a107af768f44a463f454 # 2024-10-14 17:47:13 #

    abc[  "menubar_code"     ] = Menu( abc[  "menubar" ] , tearoff = 1 ) ; abc[  "menubar" ].add_cascade( label = "Code"      , menu = abc[  "menubar_code"     ] )

    ####################################################################
    ##                          Code Options                          ##
    ####################################################################


    ####################################################################
    ##                         Code Comments                          ## Something here looks familiar
    ####################################################################

    abc[  "menubar_code__cmnt" ] = Menu( abc[  "menubar_code" ] , tearoff = 1 )

    abc[  "menubar_code" ].add_cascade( font = "TkFixedFont" , label = "Code Comments" , menu = abc[  "menubar_code__cmnt" ] )

    abc[  "menubar_code" ].add_command( font = "TkFixedFont" , label = 'Build Python List (C) from lines in (A)'                                            , command = lambda: abc__code__build_structures( **{ "fm_box":"A" , "to_box":"C" , "do_this":"py_list"                       } ) )
    abc[  "menubar_code" ].add_command( font = "TkFixedFont" , label = 'Build Python List (C) from lines in (A) with newline'                               , command = lambda: abc__code__build_structures( **{ "fm_box":"A" , "to_box":"C" , "do_this":"py_list" , "delim" : "newline" } ) )
    abc[  "menubar_code" ].add_command( font = "TkFixedFont" , label = 'Get Hash and Timestamp of function in (C)'                                          , command = lambda: abc__code__hash_function(    **{ "fm_box":"C" } ) )


    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 Center Space Pad with VS Code Folding'   , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 Center Space Pad with VS Code Folding'   , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I08 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I12 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":60 , "I":12 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 Left Pad'                                , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I08 Left Pad'                                , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":64 , "I": 8 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I12 Left Pad'                                , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":60 , "I":12 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I00 No Head. Left Pad. VS Code Folding'      , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W":72 , "I": 0 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I04 No Head. Left Pad. VS Code Folding'      , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W":68 , "I": 4 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I00 No Head. Rigth Pad. VS Code Folding'     , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W":72 , "I": 0 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I04 No Head. Rigth Pad. VS Code Folding'     , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W":68 , "I": 4 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I00 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )

    ####################################################################

    #abc[ "menubar_code"  ].add_separator()

    ####################################################################

    abc[  "menubar_code__cmnt_more" ] = Menu( abc[  "menubar_code__cmnt"    ] , tearoff = 1 )

    abc[  "menubar_code__cmnt"    ].add_cascade( font = "TkFixedFont" , label = "More Code Comments" , menu = abc[  "menubar_code__cmnt_more" ] )

    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I00 --VL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W": 72 , "I": 0 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I00 --VR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W": 72 , "I": 0 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I04 --VL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W": 68 , "I": 4 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I04 --VR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W": 68 , "I": 4 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"R" } ) )
    
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I00 CPVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I00 CPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I00 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I00 CSVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I00 CSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I00 RPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I00 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I08 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I08 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 64 , "I": 8 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I04 CPVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I04 CPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I04 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I04 CSVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I04 CSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I04 RPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I04 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I00 CPVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I00 CPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I00 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I00 CSVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I00 CSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I00 RPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I00 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W": 72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I00 CPVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I00 CPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I00 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I00 CSVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I00 CSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) , columnbreak = 1 )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I00 RPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I00 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I12 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 60 , "I":12 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I08 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I08 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 64 , "I": 8 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 CPVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 CPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 CSVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 CSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 RPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I04 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 CPVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 CPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 CSVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 CSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 RPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I00 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W": 72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I00 CP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I00 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I00 LP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 48 , "I": 0 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I00 LS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 48 , "I": 0 , "cmnt_align":"L" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I00 RP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I00 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I12 CP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 60 , "I":12 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I12 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 60 , "I":12 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I12 LP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 60 , "I":12 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I12 RP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 60 , "I":12 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I12 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 60 , "I":12 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I08 CP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) , columnbreak = 1 )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I08 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I08 LP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 64 , "I": 8 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I08 RP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 64 , "I": 8 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I08 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 64 , "I": 8 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 CP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 CPVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 CPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 CSVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 CSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 LP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 RP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 RPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I04 RSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 CP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 CPVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 CPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 CS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 CSVL'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 CSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 LP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 RP--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 RPVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 RS--'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I00 RSVR'  , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W": 72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )

    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W112 I00 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":112 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W112 I00 CP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":112 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[  "menubar_code__cmnt_more" ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W112 I00 LP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":112 , "I": 0 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )

    ####################################################################

    #abc[  "menubar_code" ].add_separator()
      
    ####################################################################
      
    #abc[  "menubar_code__options" ] = Menu( abc[  "menubar_code" ] , tearoff = 1 )
      
    #abc[  "menubar_code" ].add_cascade( font = "TkFixedFont" , label = "Options and Defaults" , menu = abc[  "menubar_code__options" ] )
      
    ### Code Options : VS Code Default Code Folding String ##############
      
    #abc[  "code_vs_code_fold" ] = StringVar()
    #abc[  "code_vs_code_fold" ].set( gopts[ "code_vs_code_fold" ] )
      
    #abc[  "menubar_code__default_code_fold" ] = Menu( abc[  "menubar_code__options" ] , tearoff = 1 )
      
    #abc[  "menubar_code__options" ].add_cascade( font = "TkFixedFont" , label = "VS Code. Default Fold Langauge" , menu = abc[  "menubar_code__default_code_fold" ] )
      
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''Perl5                  #region           #endregion'''           , value = 10 , variable=abc[ "code_vs_code_fold" ] ) #  Perl5:                 |#region           |#endregion             |=pod          |=cut           
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''PowerShell             #region           #endregion'''           , value = 10 , variable=abc[ "code_vs_code_fold" ] ) #  PowerShell:            |#region           |#endregion             |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''C#                     #region           #endregion'''           , value = 10 , variable=abc[ "code_vs_code_fold" ] ) #  C#:                    |#region           |#endregion             |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''Python                 #region           #endregion'''           , value = 10 , variable=abc[ "code_vs_code_fold" ] ) #  Python:                |#region           |#endregion             |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''PHP                    #region           #endregion'''           , value = 10 , variable=abc[ "code_vs_code_fold" ] ) #  PHP:                   |#region           |#endregion             |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''VB                     #Region           #End Region'''          , value = 11 , variable=abc[ "code_vs_code_fold" ] ) #  VB:                    |#Region           |#End Region            |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''shellscript            # region          # endregion'''          , value = 12 , variable=abc[ "code_vs_code_fold" ] ) #  shellscript:           |# region          |# endregion            |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''TypeScript/JavaScript  //#region         //#endregion'''         , value = 20 , variable=abc[ "code_vs_code_fold" ] ) #  TypeScript/JavaScript: |//#region         |//#endregion           |// #region    |// #endregion  
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''F#                     //#region         //#endregion'''         , value = 20 , variable=abc[ "code_vs_code_fold" ] ) #  F#:                    |//#region         |//#endregion           |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''Java                   //#region         //#endregion'''         , value = 20 , variable=abc[ "code_vs_code_fold" ] ) #  Java:                  |//#region         |//#endregion           |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''Golang                 //region          //endregion'''          , value = 21 , variable=abc[ "code_vs_code_fold" ] ) #  Golang:                |//region          |//endregion            |//#region     |//#endregion   
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''SCSS/Less              // #region        // #endregion'''        , value = 22 , variable=abc[ "code_vs_code_fold" ] ) #  SCSS/Less:             |// #region        |// #endregion          |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''Go                     // #region        // #endregion'''        , value = 22 , variable=abc[ "code_vs_code_fold" ] ) #  Go:                    |// #region        |// #endregion          |// region     |// endregion   
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''C/C++                  #pragma region    #pragma endregion'''    , value = 30 , variable=abc[ "code_vs_code_fold" ] ) #  C/C++:                 |#pragma region    |#pragma endregion      |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''Bat                    ::#region         ::#endregion'''         , value = 31 , variable=abc[ "code_vs_code_fold" ] ) #  Bat:                   |::#region         |::#endregion           |REM #region   |REM #endregion 
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''sql                    --#region         --#endregion'''         , value = 32 , variable=abc[ "code_vs_code_fold" ] ) #  sql:                   |--#region         |--#endregion           |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''Markdown               <!-- #region -->  <!-- #endregion -->'''  , value = 90 , variable=abc[ "code_vs_code_fold" ] ) #  Markdown:              |<!-- #region -->  |<!-- #endregion -->    |              |               
    #abc[  "menubar_code__default_code_fold"  ].add_radiobutton( font = "TkFixedFont" , label = r'''CSS/SCSS/Less          /* #region */     /* #endregion */'''     , value = 91 , variable=abc[ "code_vs_code_fold" ] ) #  CSS/SCSS/Less:         |/* #region */     |/* #endregion */       |/*#region*/   |/*#endregion*/ 

# endregion  ## Code Menu ############################################




########################################################################
##                           Code Functions                           ##
########################################################################

# region     # Code Functions ##########################################

def abc__code__fancy_comments( **kwargs ) :  ## 6a3b1c44f856adfea9381e438f3ea8a3 # 2024-04-01 00:27:50 #
    
    fm_box      = kwargs.get( "fm_box"    , "A" )
    to_box      = kwargs.get( "to_box"    , "C" )
    cmnt_head   = kwargs.get( "head"      , "2" )
    cmnt_width  = kwargs.get( "W"         , 72  )
    cmnt_indent = kwargs.get( "I"         ,  0  ) ; cmnt_indent = " "*cmnt_indent
    fold_type   = kwargs.get( "fold_type" , "-" )
    cmnt_align  = { "L" : "<" , "C" : "^" , "R" : ">" }.get( kwargs.get( "cmnt_align" ) , "R" )
    fold_align  = { "L" : "<" , "C" : "^" , "R" : ">" }.get( kwargs.get( "fold_align" ) , "L" )
    cmnt_pad    = { "S" : " " , "P" : "#" }.get( kwargs.get( "cmnt_pad" ) , "S" )


    cmnts = [ x.strip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() if x and x.strip() ]

    _clear_box( to_box )
    
    cmnt_out = []

    for cmnt in cmnts :

        if cmnt_head == 1 :

            pw0  = cmnt_width - 4

            x = ( 
                 f'''{cmnt_indent}##{'':#^{pw0}}##\n'''
                 f'''{cmnt_indent}##{'':{cmnt_pad}^{pw0}}##\n'''
                 f'''{cmnt_indent}##{f'{f" {cmnt} "}':{cmnt_pad}{cmnt_align}{pw0}}##\n'''
                 f'''{cmnt_indent}##{'':{cmnt_pad}^{pw0}}##\n'''
                 f'''{cmnt_indent}##{'':#^{pw0}}##\n'''
                 )

            box[ to_box ].insert( "end" , f'{x}\n' )

        if cmnt_head == 2 :

            pw0  = cmnt_width - 4

            x = ( 
                 f'''{cmnt_indent}##{'':#^{pw0}}##\n'''
                 f'''{cmnt_indent}##{f'{f" {cmnt} "}':{cmnt_pad}{cmnt_align}{pw0}}##\n'''
                 f'''{cmnt_indent}##{'':#^{pw0}}##\n'''
                 )

            box[ to_box ].insert( "end" , f'{x}\n' )

        if cmnt_head == 3 :

            pw0  = cmnt_width - 4

            x = f'''{cmnt_indent}##{f'{f" {cmnt} "}':{cmnt_pad}{cmnt_align}{pw0}}##\n'''

            box[ to_box ].insert( "end" , f'{x}\n' )

        if fold_type == "V" :

            pw0  = cmnt_width - 15

            x = ( 
                 f'''{cmnt_indent}#region    ##{f'{f" {cmnt} "}':#{fold_align}{pw0}}##\n\n'''
                 f'''{cmnt_indent}#endregion ##{f'{f" {cmnt} "}':#{fold_align}{pw0}}##\n'''
                 )

            box[ to_box ].insert( "end" , f'{x}\n' )


def abc__code__build_structures( **kwargs ) :  ## f8b75ac47da1efaa378ef8a2085fe656 # 2024-04-01 00:25:31 #

    fm_box  = kwargs.get( "fm_box"  , "A"      )
    to_box  = kwargs.get( "to_box"  , fm_box   )
    do_this = kwargs.get( "do_this" , "py_lst" )
    delim   = kwargs.get( "delim"   , None     )

    timenow = datetime.datetime.now()

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__code__build_structures( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" , "do_this" : "{do_this}" }} )' )

    if   do_this == "py_list" :

        lst_to = []
        
        for v in [ x for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() if x and x.strip() ] :

            lst_val = None

            if   ( lst_val := re.match( r'^\'\'\'(.*)\'\'\'$' , v ) ) : lst_val = lst_val.group(1)
            elif ( lst_val := re.match( r'^\"\"\"(.*)\"\"\"$' , v ) ) : lst_val = lst_val.group(1)
            elif ( lst_val := re.match( r'^\'(.*)\'$'         , v ) ) : lst_val = lst_val.group(1)
            elif ( lst_val := re.match( r'^\"(.*)\"$'         , v ) ) : lst_val = lst_val.group(1)
            elif ( lst_val := re.match( r'^(..*)$'            , v ) ) : lst_val = lst_val.group(1)

            if lst_val :

                if   not re.search( r'(?:\'\'\'|\"\"\"|\")' , lst_val ) : lst_to.append( f'"{lst_val}"' )
                elif not re.search( r'(?:\'\'|\"\"\"|\')'   , lst_val ) : lst_to.append( f"'{lst_val}'" )
                elif not re.search( r'\"'                   , lst_val ) : lst_to.append( f'"{lst_val}"' )
                elif not re.search( r'\''                   , lst_val ) : lst_to.append( f"'{lst_val}'" )
                else : print( f'# WARN # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__code__build_structures # Failed to match this : {lst_val}' )

        if lst_to :
            
            _clear_box( to_box )

            #if   delim == "newline" : print( 'my_list = [ \n      ' + "\n    , ".join(lst_to) + '\n    ]\n' )
            #else                    : print( 'my_list = [ ' + " , ".join(lst_to) + ' ]\n' )

            if   delim == "newline" : box[ to_box ].insert( "end" , 'my_list = [ \n      ' + "\n    , ".join(lst_to) + '\n    ]\n' )
            else                    : box[ to_box ].insert( "end" , 'my_list = [ ' + " , ".join(lst_to) + ' ]\n' )
         

def abc__code__hash_function( **kwargs ) :  ## 20b7687a13ee105e1a6815026cd1adb2 # 2024-04-10 11:05:51 #
    
    #todo : add if and elif statements too

    timenow = datetime.datetime.now()

    fm_box  = kwargs.get( "fm_box"  , "C" )
    to_box  = kwargs.get( "to_box"  , fm_box )

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__code__hash_function( {{ "fm_box" : "{fm_box}" }} )' )

    lst_orig = [ x.rstrip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    if not lst_orig :
        print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__code__hash_function : Nothing found to hash.' )
        return

    ## #todo: Remove leading lines until a reserved word shows up: def, sub , if, elsif, elif, function, int, module, fn
    while lst_orig :
        if ( re.match( r"^$"    , lst_orig[0] ) ) : 
            lst_orig.pop(0)
            continue
        if ( re.match( r"^\s*#" , lst_orig[0] ) ) : 
            lst_orig.pop(0)
            continue
        break

    ## Remove Current fingerprint
    if (func_name := re.search( r"^(def .*\))\s*:(?:\s\s*#..*)?$" , lst_orig[0] ) ) :
        lst_orig[0] = f'{func_name.group(1)} : '
    
    lst_hash = []
    
    ## Remove lines that do not need to be hashed
    for x in lst_orig :
        if ( re.match( r"^$"    , x ) ) : continue
        if ( re.match( r"^\s*#" , x ) ) : continue
        lst_hash.append(x)

    if lst_hash :
        str_md5 = "\n".join( lst_hash )
        str_md5 = hashlib.md5(str_md5.encode()).hexdigest()
        lst_orig[0] = f'{lst_orig[0]} ## {str_md5} # {timenow:%Y-%m-%d %H:%M:%S} #'

        _clear_box( "A" )
        _clear_box( "B" )

        box[ "A" ].insert( "end" , '################################################\n' )
        box[ "A" ].insert( "end" , '##               Original Code                ##\n' )
        box[ "A" ].insert( "end" , '################################################\n' )
        box[ "A" ].insert( "end" , '\n' )
        box[ "A" ].insert( "end" , "\n".join(lst_orig) + '\n' )

        box[ "B" ].insert( "end" , '################################################\n' )
        box[ "B" ].insert( "end" , '##                Code Hashed                 ##\n' )
        box[ "B" ].insert( "end" , '################################################\n' )
        box[ "B" ].insert( "end" , '\n' )
        box[ "B" ].insert( "end" , "\n".join(lst_hash) + '\n' )


# endregion  # Code Functions ##########################################



###############################################################################################################
#                                                                                                             #
#                                       #     #   ###    #####   #####                                        #
#                                       ##   ##    #    #     # #     #                                       #
#                                       # # # #    #    #       #                                             #
#                                       #  #  #    #     #####  #                                             #
#                                       #     #    #          # #                                             #
#                                       #     #    #    #     # #     #                                       #
#                                       #     #   ###    #####   #####                                        #
#                                                                                                             #
###############################################################################################################









####################################################################
##                           Misc Menu                            ##
####################################################################

# region     ## Misc Menu ##########################################

def menubar_misc() :  ## 0575da1a13091478a828df3121d6e815 # 2024-10-14 17:51:00 #

    abc[  "menubar_misc"     ] = Menu( abc[  "menubar" ] , tearoff = 1 ) ; abc[  "menubar" ].add_cascade( label = "Misc"      , menu = abc[  "menubar_misc"     ] )

    ####################################################################
    ##                Misc Menu : Generate Random Data                ##
    ####################################################################

    abc[  "menubar_misc_random"  ] = Menu( abc[  "menubar_misc" ] , tearoff = 1 )

    abc[  "menubar_misc" ].add_cascade( font = "TkFixedFont" , label = "Generate Random Data" , menu = abc[  "menubar_misc_random"  ] )

    abc[  "menubar_misc_random" ].add_command( font = "TkFixedFont" , label = 'X Y Decimal Coordinates (C)'               , command = lambda: abc__misc__gen_random_data( "C" , "xy coords" ) )
    abc[  "menubar_misc_random" ].add_command( font = "TkFixedFont" , label = 'Y X Decimal Coordinates (C)'               , command = lambda: abc__misc__gen_random_data( "C" , "yx coords" ) )
    abc[  "menubar_misc_random" ].add_command( font = "TkFixedFont" , label = 'Epoch dates (C)'                           , command = lambda: abc__misc__gen_random_data( "C" , "epoch"     ) )
    abc[  "menubar_misc_random" ].add_command( font = "TkFixedFont" , label = 'Generate Random Chars/Password'            , command = lambda: abc__misc__generate_password( **{ "fm_box":"A" } ) )

# endregion  ## Misc Menu ##########################################


########################################################################
##                           Misc Functions                           ##
########################################################################

# region     # Misc Functions ##########################################

def abc__misc__gen_random_data( to_box , do_this ) :  ## 28276328f4ab015a5192ae3d6053c109 # 2024-04-10 11:08:34 #

    timenow = datetime.datetime.now()

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__gen_random_data( {{ "to_box" : "{to_box}" , "do_this" : "{do_this}" }} )' )

    _clear_box( to_box )

    if do_this == "xy coords" :

        for _ in range(100) :

            x = ( 360 * random.random() ) - 180
            y = ( 180 * random.random() ) -  90

            box[ to_box ].insert( "end" , f'{x:.6f},{y:.6f}\n' )

    elif do_this == "yx coords" :

        for _ in range(100) :

            x = ( 360 * random.random() ) - 180
            y = ( 180 * random.random() ) -  90

            box[ to_box ].insert( "end" , f'{y:.6f},{x:.6f}\n' )

    elif do_this == "epoch" :

        x = datetime.datetime.now().timestamp()

        for _ in range(100) :

            y = int( x - ( ( 86400 * 365 * 10 ) * random.random() ) )

            box[ to_box ].insert( "end" , f'{y}\n' )


def abc__misc__generate_password( **kwargs ) :  ## 46feb3eea1aea125bcffafc724e0c0c5 # 2024-10-14 17:56:50 #

    timenow = datetime.datetime.now()

    to_box  = kwargs.get( "to_box"  , "C"   )
    
    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password( {{ "to_box" : "{to_box}" }} )' )
    #print( f'# DONE # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password : MS 24 Charset' )
    #print( f'# DONE # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password : Easy4' )
    #print( f'# DONE # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password : lowers' )
    #print( f'# DONE # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password : uppers' )
    #print( f'# DONE # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password : alphas' )
    #print( f'# DONE # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password : alphanumerics' )
    #print( f'# DONE # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password : alpha numeral specials' )
    print( f'# TODO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__misc__generate_password : DH passbook' )

    austin_words  = set()
    austin_words |= { "able","adds","airs","alas","also","amid","anew","anne","arch","army","arts","aunt","away","awed","back","ball","balm","bare","bath","bear","been","begs","bell","bent","best","bets","blow","blue","body","bold","book","bore","born","both","bowl","bows","boys","brow","busy","cake","call","calm","came","camp","card","care","case","cast","chin","city","clue","coat","cold","come","cook","cool","cost","cows","dale","damp","dare","dark","date","days","dead","deal","dear","debt","deep","defy","deny","died","dine","dirt","dish","does","done","door","dose","dove","down","draw","drew","drop","duel","dull","dupe","duty","each","earl","ease","easy","echo","edge","else","envy","even","ever","evil","eyes","face","fact","fail","fair","fall","fame","fare","farm","fast","fate","fear","feel","feet","fell","felt","fill","find","fine","fire","firm","fish","five","flat","flew","flow","fond","fool","foot","form","foul","four","free","fret","from","full","fuss","gain","game","gate","gave","gaze","gets","gift","girl","give","glad","glen","glow","goes","gone","good","gown","grew","grow","gulf","hack","hair","half","hall","hand","hang","hard","harm","harp","hate","have","haye","head","heal","hear","held","help","here","hers","hide","high","hill","hint","hire","hold","home","hope","hour","hurt","idea","idle","inns","into","jane","jilt","john","join","joke","july","june","just","keep","kent","kept","kill","kind","king","kiss","knew","know","lace","lady","laid","land","lane","last","late","lawn","lead","left","lend","less","lest","lies","lieu","life","lift","like","line","lips","list","live","lock","long","look","lord","lose","loss","lost","loud","love","luck","made","maid","make","male","many","mark","mary","mean","meat","meet","mend","mere","mess","mien","mild","mile","mind","mine","miss","mode","more","most","move","much","must","name","near","neat","need","news","next","nice","nine","nods","none","noon","nose","note","oaks","obey","omen","omit","once","ones","only","open","ours","over","owed","owes","owns","pace","pack","page","paid","pain","pair","pale","pang","papa","park","part","pass","past","path","peak","peep","pens","pigs","pity","plan","play","pool","poor","port","post","pour","pray","prey","pull","pure","quit","race","rage","rail","rain","rang","rank","rant","rate","read","real","reap","reel","rein","rely","rest","rich","ride","ring","rise","risk","road","rode","room","rose","rude","ruin","rule","runs","safe","said","sake","same","sang","sash","save","says","seat","seek","seem","seen","sees","self","sell","send","sent","sept","shed","shew","shop","show","shut","sick","side","sigh","sign","sing","sink","size","slit","slow","snug","sole","some","song","sons","soon","sore","sort","soul","soup","sour","spot","spur","stay","stem","step","stir","stop","such","suit","sunk","sure","take","talk","tall","tear","tell","tend","tens","tent","term","test","than","that","them","then","they","thin","this","thus","tide","till","time","told","tone","took","tour","town","trim","true","turn","ugly","undo","upon","used","vain","vary","vast","vent","very","vice","view","void","vows","wait","walk","want","ward","warm","warn","wave","ways","weak","wear","week","weep","well","went","were","west","what","when","whom","wide","wife","wild","will","wind","wine","wink","wise","wish","with","wits","wood","word","wore","work","worn","yawn","year","york","your","abide","abode","about","above","abuse","ached","acted" }
    austin_words |= { "acute","added","adept","adieu","admit","adopt","after","again","agony","agree","aimed","alarm","alike","alive","allow","alone","along","aloof","aloud","altar","alter","amaze","amiss","among","ample","amply","amuse","angel","anger","angry","ankle","annum","apace","apply","april","arise","arose","aside","asked","atone","aught","aunts","avail", "avoid","awake","aware","awful","awoke","balls","banks","basis","bears","beaux","began","begin","begun","being","below","bills","birds","birth","black","blame","bless","blind","blots","blown","blush","board","boast","books","borne","bosom","bound","bowed","boxes","brain","break","bribe","bride","bring","brink","broke","brown","build","built", "burnt","burst","calls","cards","cared","cares","carry","cases","catch","cause","cease","cents","chair","charm","cheap","cheat","check","chief","child","china","chose","civil","claim","class","clear","clerk","clock","close","clump","coach","coats","colds","comes","cooks","copse","corps","cough","could","court","cover","cried","cross","crowd", "crown","cruel","daily","dance","darcy","dared","dated","death","debts","defer","delay","denny","deter","dined","dines","dirty","doing","doors","doubt","dozen","drawn","dread","dress","drily","drink","drive","dropt","drove","ducks","duets","duped","dwell","dwelt","dying","eager","early","earth","eclat","edged","eight","elder","eliza","elope", "ended","enemy","enjoy","ensue","enter","epsom","equal","error","evade","event","every","evils","exact","excel","exert","exist","faces","facts","faint","falls","false","fancy","fault","favor","fears","feels","fetch","fewer","field","fifty","fight","final","finds","finer","first","fixed","flirt","folly","force","forms","forth","forty","found", "frame","fresh","front","frost","fruit","fully","gaily","gaped","gates","gaudy","gayer","girls","given","gives","glass","gloom","glory","glove","going","gowns","grace","grain","grand","grasp","grave","great","green","grief","gross","group","grove","grown","guard","guess","guest","guide","guilt","habit","hands","happy","haste","hasty","hated", "hates","haunt","heads","heard","hears","heart","heavy","hedge","heirs","hence","hills","hints","hired","hoped","hopes","horse","hotel","hours","house","human","hurry","hurts","ideas","imply","incur","irish","james","jewel","jokes","judge","jumps","keeps","kinds","kitty","knees","known","knows","laity","lakes","lanes","large","later","laugh", "leads","learn","lease","least","leave","legal","lewis","light","liked","likes","lines","lived","lives","lizzy","lobby","local","lodge","lofty","looks","loose","loser","loved","lover","loves","lower","lucas","lucky","lydia","lying","madam","makes","mamma","manor","march","maria","marks","marry","match","means","meant","meets","merit","merry", "might","miles","minds","mirth","mixed","model","money","month","moral","mount","mouth","moved","music","named","names","nasty","never","niece","night","noble","noise","noisy","north","notes","occur","oddly","offer","often","older","order","other","ought","owing","owned","owner","pages","pains","paint","paler","pales","paper","parts","party", "pause","peace","piece","place","plain","plans","plate","plays","plead","point","pools","power","pratt","press","price","pride","prior","prone","proof","proud","prove","proxy","punch","purse","quest","quick","quiet","quite","range","rapid","rated","reach","ready","repel","reply","ridge","right","rings","risen","rises","rites","rival","river", "roads","rocks","rooms","rough","round","route","sadly","sakes","salad","sally","sarah","satin","saucy","saved","scale","scene","scold","scope","score","scorn","seats","seems","seize","sends","sense","serve","seven","shade","shake","shall","shame","shape","share","sharp","sheet","shift","shine","shire","shock","shoes","shook","shoot","shops", "short","shown","shows","shrug","sides","sight","signs","silly","since","sings","sixth","sized","skill","slave","sleep","slept","small","smart","smile","sneer","sofas","solid","songs","sorry","sound","south","space","spare","spars","speak","speed","spend","spent","spite","spoke","sport","spots","stage","staid","stamp","stand","start","state", "stays","steps","still","stirs","stoke","stole","stone","stood","store","storm","story","stout","study","style","sweet","swell","table","tacit","taken","takes","talks","taste","teach","tears","tease","teeth","tells","tempt","tenor","tents","terms","thank","their","there","these","thing","think","third","those","three","threw","throw","timed", "times","tired","tires","title","token","topic","total","trace","trade","train","trait","treat","trees","tress","trial","tried","tries","troop","trout","truly","trunk","trust","truth","turns","twice","uncle","under","unfit","union","unite","until","upper","urged","using","usual","utter","vague","valid","value","vexed","vices","views","visit", "vogue","voice","vouch","walks","wants","waste","watch","water","wears","weary","weeks","where","which","while","whims","whist","white","whole","whose","widow","wiser","witty","wives","woman","women","woods","woody","words","world","worse","worst","worth","would","wound","write","wrong","wrote","yards","years","yield","young","yours","youth" }
    austin_words |= { "abound","abroad","abrupt","absent","absurd","abused","accede","accent","accept","accuse","acquit","across","acting","action","active","actual","adding","adieus","admire","advice","advise","affair","affect","afford","afraid","afresh","agreed","airing","alarms","allude","almost","always","amazed","amazes","amends","amidst","amount","amused", "animal","ankles","annual","answer","anyhow","anyone","appeal","appear","archly","ardent","argued","arisen","around","arrear","arrive","artful","asking","aspect","aspire","assent","assert","assist","assume","assure","atoned","attach","attack","attend","attics","august","austen","avenue","avowal","avowed","backed","banish","barely","barnet", "beauty","became","become","befall","before","begged","begins","behalf","behave","beheld","behind","belief","belong","bestow","betray","better","beyond","biting","bitter","blamed","blinds","blowsy","bodies","boldly","bonnet","borrow","bosoms","bottle","bottom","bought","bounds","bounty","bourgh","bowing","brains","branch","breach","breast", "breath","bridge","bright","brings","broken","busily","bustle","butler","buying","calico","called","calmly","candid","cannot","canvas","capers","caring","carter","carved","casual","caught","caused","causes","ceased","chaise","chance","change","charge","charms","chatty","cheeks","choice","choose","chosen","church","circle","claims","clarke", "clergy","clever","closed","closer","closet","coarse","coaxed","coffee","cogent","colder","coldly","colour","coming","common","comply","convey","coolly","copied","corner","coughs","county","couple","course","cousin","covies","credit","crying","custom","danced","dances","danger","daring","dawson","deaden","dearly","decent","decide","decked", "deemed","deeper","deeply","defect","defend","defied","degree","demand","demean","denial","denied","depart","depend","derive","desert","design","desire","detail","detain","detect","detest","device","devoid","devote","differ","dining","dinner","direct","disarm","dishes","dismay","divert","divide","doings","double","doubly","doubts","driven", "during","duties","easily","easter","eating","effect","effort","either","elated","eldest","eleven","eloped","eluded","employ","enable","endure","energy","engage","enough","ensign","ensued","ensure","entail","envied","equals","errand","errors","escape","estate","esteem","events","exceed","except","excess","excite","excuse","expect","expose", "extent","extort","eyeing","failed","fairly","fallen","family","father","faults","faulty","favour","feared","fellow","female","fender","fidget","fields","figure","filial","filled","finery","finest","finish","firmly","fitted","fixing","flight","flowed","flying","folded","folios","follow","fonder","forbid","forced","forego","forget","forgot", "formal","formed","former","fourth","freely","french","friday","friend","frisks","fruits","fulfil","future","gaiety","gained","gaming","garden","genius","gentle","george","giving","gladly","glance","gloomy","godson","graces","grapes","gravel","gretna","griefs","grieve","ground","growth","guests","guided","guilty","guinea","habits","handed", "happen","hardly","hasten","hating","hatred","haunch","having","health","hearth","hearty","heaven","height","higher","highly","hinted","hither","honest","honour","hoping","horrid","horror","horses","hotels","houses","humble","humour","hursts","hushed","impose","impute","inches","income","indeed","induce","infamy","inform","injure","injury", "inmate","insist","intend","inured","invent","invite","itself","jewels","joined","joints","joking","joyful","judged","jumped","junior","justly","keener","killed","kinder","kindly","kissed","labour","ladies","lagged","lament","larder","larger","lasted","lastly","lately","latest","latter","laurel","laying","learnt","leaves","legacy","length", "lessen","lesson","letter","liable","lifted","likely","liking","limits","listen","little","lively","livery","living","lodges","london","longed","longer","looked","losing","losses","louder","loudly","louisa","lovely","lovers","loving","lowest","lustre","maiden","making","malice","manage","manner","marked","market","master","matter","mature", "meanly","member","memory","merely","merits","method","middle","mildly","miller","minute","misery","misled","missed","mixing","modern","modest","moment","monday","months","morrow","mortal","mostly","mother","motion","motive","mouths","moving","muffin","muslin","mutual","myself","naming","narrow","nature","nearer","nearly","needed","nephew", "nerves","newest","nicely","nicest","nieces","nobler","nobody","notice","notion","novels","number","oakham","obeyed","object","oblige","obtain","occupy","occurs","oclock","oddity","odious","offend","offers","office","opened","openly","oppose","orders","others","outrun","oxford","packed","paling","paltry","papers","parade","pardon","parent", "parish","parted","partly","passed","patron","paused","pauses","paying","people","period","permit","person","pieces","piling","piqued","piquet","pitied","placed","places","plague","played","please","plenty","pocket","poetry","points","policy","polite","ponies","poorly","pounds","poured","powers","praise","prefer","pretty","prided","prized", "prizes","profit","prompt","proper","proved","public","puffed","pulvis","punish","purses","pursue","puzzle","racked","ragout","rained","raised","ramble","rather","rattle","reader","really","reason","rebuke","recall","recede","recent","reckon","rector","refuge","refuse","refute","regain","regard","regret","reject","relate","relied","relief", "remain","remark","remedy","remind","remove","render","repaid","repeat","repent","repine","report","repose","rescue","resent","resign","resist","rested","result","resume","retail","retain","retort","return","review","revive","revolt","richly","riding","rising","rivals","rivers","roused","ruined","rushed","safely","safest","safety","saloon", "savage","saving","saying","scarce","scenes","scheme","school","scores","scotch","scrape","screen","search","season","seated","second","secret","secure","sedate","seeing","seemed","seized","seldom","selves","senses","sequel","sermon","settle","severe","shades","shaken","shared","sheets","shewed","shield","should","showed","shrink","sickly", "sighed","signal","silent","simple","simply","single","sister","sketch","slight","slowly","smiled","smiles","smirks","social","solace","solely","solemn","sonnet","sooner","soothe","sorely","sorrow","sought","sounds","source","spared","spasms","speaks","speech","speedy","sphere","spirit","spleen","spoilt","spoken","sports","sprang","spread", "spring","stairs","stands","stared","starve","stated","stayed","steady","stiles","straws","stream","street","stress","strike","stroke","stroll","strong","struck","stuffy","stupid","submit","sudden","suffer","suited","summer","summon","sunday","supper","supply","surely","surest","survey","tables","tackle","taking","talent","talked","talker", "taller","tanned","tastes","taught","teased","temper","tenant","tender","termed","thanks","theirs","thence","things","thinks","thirty","though","throat","thrown","tithes","tongue","topics","toward","traced","traces","trials","tricks","trifle","truest","trunks","trying","tumult","turned","twelve","twenty","uglier","unable","uncles","undone", "uneasy","unfelt","unfold","united","unjust","unless","unlike","untidy","unwell","uproar","urgent","useful","utmost","vacant","valley","valued","vanish","vanity","varied","vastly","verily","verses","vexing","victim","vigour","virtue","visits","volume","vulgar","waited","waiter","waived","waking","walked","walker","wander","wanted","warded", "warmly","warmth","warned","wealth","weight","whence","whilst","wholly","widely","wilful","window","winter","wisdom","wisely","wisest","wished","wishes","within","wonder","worked","worthy","writer","writes","yawned","youths" }
    austin_words |= { "abiding","absence","abusing","abusive","acceded","accents","account","accused","acquire","actions","acutely","acutest","adapted","address","adhered","admired","admirer","admires","adopted","adorned","advance","advised","affable","affairs","affords","affront","against","agonies","alarmed","allayed","allowed","alluded","already","altered", "amazing","amiable","amongst","amusing","ancient","angelic","angrily","anguish","annexed","annoyed","another","answers","anxiety","anxious","anybody","apology","apparel","appeals","appears","appease","applied","applies","approve","arguing","arising","aroused","arrange","arrival","arrived","article","ashamed","assents","assumed","assured", "attacks","attempt","audible","augment","availed","avarice","avoided","awaited","awkward","bandbox","bashful","battled","bearing","because","becomes","begging","behaved","behaves","believe","belongs","beloved","benches","beneath","benefit","bequest","besides","between","bidding","bingley","blacken","blaming","blasted","blemish","blessed", "blinded","blushed","boasted","brevity","bribery","briefly","britain","british","brittle","bromley","brother","brought","burning","burying","butcher","calling","cambric","campful","candour","capable","capital","caprice","captain","careful","carpets","carried","cassino","caution","censure","certain","chagrin","chamber","chanced","chances", "changed","changes","chapter","charged","charity","charles","checked","cherish","chicken","chiefly","chooses","circles","circuit","civilly","claimed","clapham","cleanse","cleared","clearer","clearly","clement","closely","closest","closure","clothes","clouded","cluster","collect","colonel","comfort","command","company","compare","compass", "compose","conceal","conceit","concern","concise","condemn","condole","conduct","confess","confide","confirm","connect","conquer","consent","consign","console","consult","contain","content","convert","cooking","cordial","correct","costing","counted","country","couples","courage","courier","courses","courted","cousins","covered","cradles", "crammed","crayons","created","crossed","crowded","crowned","cruelly","cruelty","culprit","cunning","curious","curtsey","custody","cutting","dancing","darling","darting","dawdled","dearest","decease","deceive","decency","decided","declare","decline","decorum","deduced","deepest","default","defects","defence","defense","defined","degrees", "deigned","delayed","delight","demands","denoted","denying","deprive","derived","derives","descent","deserts","deserve","designs","desired","despair","despise","develop","devoted","dictate","diffuse","dignity","dinners","discern","discuss","disdain","disgust","dislike","display","dispose","dispute","distant","disturb","divided","doleful", "doorway","doubled","doubted","drawing","dreaded","dressed","dresses","driving","dropped","duchess","dullest","eagerly","earlier","earnest","earthly","economy","ecstasy","effects","efforts","elapsed","elderly","elegant","elevate","eloping","embargo","eminent","emotion","enabled","endless","endured","enemies","engaged","england","engross", "enhance","enraged","ensuing","entered","entreat","envying","epithet","equally","escaped","essence","estates","evening","evident","exactly","examine","example","excited","exclude","excused","excuses","exerted","exhibit","existed","expects","expence","expense","explain","explore","exposed","express","extreme","failing","failure","fainter", "faintly","fairest","falling","falsely","fancied","farther","fashion","fatigue","favours","fearful","fearing","feather","feature","feeling","fellows","females","fervent","fetched","fidgets","fidgety","fifteen","figures","filling","finally","finding","fingers","firmest","fishing","flaming","flatter","flogged","flowing","flutter","follies", "follows","foolish","footing","footman","forbade","forbore","forcing","fordyce","foresaw","foresee","forever","forfeit","forgave","forgets","forgive","forlorn","forming","forster","fortune","forward","founded","frailty","frankly","freedom","fresher","friends","fronted","fullest","furnish","further","gaining","gallant","gallery","general", "genteel","genuine","getting","glazing","glimpse","gloried","glories","glowing","gradual","gratify","gravely","gravity","greater","greatly","grieved","grounds","grouped","growing","guarded","guessed","guiding","hackney","hanging","happens","happier","happily","hardest","harmony","harriet","harshly","hastily","haughty","hauteur","healthy", "hearers","hearing","heavens","heavier","heinous","heiress","herself","highest","himself","history","holding","honours","however","humbled","hundred","hunting","hurried","husband","illness","imagine","imitate","immoral","implied","implies","imposed","improve","impulse","imputed","include","induced","indulge","infancy","inflict","informs", "inherit","injured","inmates","inquire","inquiry","insipid","insists","inspire","instant","instead","intrude","invalid","invited","involve","irksome","italian","january","jealous","joining","journey","judging","jumbled","jumping","justice","justify","keenest","keeping","kindest","kindred","kingdom","kitchen","knowing","kympton","laconic", "lambton","landing","languor","largest","lasting","laughed","leading","leaning","learned","leaving","legally","leisure","letters","letting","liberal","liberty","library","licence","lighted","livings","longing","looking","lottery","lowness","lucases","luckily","lurking","managed","manager","mankind","manners","mansion","married","masters", "matlock","matters","meadows","meanest","meaning","measure","meeting","mention","merited","meryton","message","metcalf","militia","mindful","mingled","minuted","minutes","miserly","mislead","missent","missing","mistake","mistook","misused","mixture","modesty","moments","monthly","morning","motives","mrdarcy","mrdenny","mrhurst","mrjones", "mrshill","mrslong","mrstone","murmurs","musical","muslins","mystery","natural","natured","nearest","neglect","neither","nephews","nervous","netting","nettled","noblest","nothing","noticed","notions","novelty","nowhere","nursing","objects","obliged","observe","obvious","october","offence","offense","offered","officer","oftener","omitted", "opening","opinion","opposed","ordered","orderly","outdone","overset","packing","paddock","painful","paining","painter","palings","panting","parasol","parcels","parents","parlour","partake","partial","parties","parting","partner","passage","passing","passion","patient","pausing","payment","peaches","peevish","penance","perfect","perform", "perhaps","periods","persist","persons","perusal","phaeton","philips","picture","pitched","pitiful","placing","plainer","plainly","planned","players","playful","playing","pleaded","pleased","pleases","pledged","pliancy","pointed","pompous","popular","portion","possess","poultry","pouring","poverty","praised","praises","predict","prepare", "present","preside","pressed","presume","pretend","prevail","prevent","private","probity","proceed","process","procure","produce","profess","profuse","project","promise","promote","propose","protest","proudly","proverb","provide","proving","provoke","prudent","publish","puddles","purport","purpose","pursued","pursuit","putting","puzzled", "quality","quarrel","quarter","quickly","quieted","quieter","quietly","quitted","raising","rallied","rambled","rapidly","rapture","reached","readily","reading","reasons","receipt","receive","recital","recover","rectory","redress","reduced","reflect","refrain","refusal","refused","regrets","regular","rejoice","related","relates","release", "relieve","remains","remarks","remorse","removal","removed","renewal","renewed","repined","replete","replied","replies","reports","repress","reproof","reputed","request","require","reserve","resides","resolve","respect","retains","retired","returns","revenge","revered","reverie","reverse","revival","revived","richard","rightly","roasted", "rosings","ruining","running","sallied","satisfy","savours","scarlet","schemes","science","scolded","scorned","screens","scruple","secrecy","secrets","secured","seeking","seeming","seizing","selfish","sending","serious","sermons","servant","service","serving","setting","settled","several","shaking","sharers","sharing","shelves","shocked", "shorten","shorter","shortly","showing","shyness","signify","silence","similar","simpers","sincere","singing","singled","sinking","sisters","sitting","sixteen","slacken","sleeves","sloping","slyness","smiling","society","solaced","solicit","somehow","someone","soothed","sources","spanish","speaker","special","spirits","springs","spurned", "stables","stanzas","started","stately","stating","station","staying","stepped","steward","stiffly","stopped","storing","stoutly","strange","streets","stretch","studied","studier","studies","subject","subjoin","subsist","succeed","success","suffers","suggest","suiting","summons","support","suppose","surmise","surpass","survive","suspect", "suspend","swelled","symptom","talents","talking","tallest","teasing","tedious","telling","tempers","tempted","tenants","thanked","theatre","thereby","therein","thirdly","thither","thought","threats","through","tickets","tidings","tongues","torment","totally","touched","towards","treated","tremble","tribute","trifled","triumph","trouble", "trusted","tuesday","turning","unasked","unaware","uncivil","unequal","unhappy","unheard","uniform","uniting","unknown","unlucky","unmoved","untamed","unusual","upstart","useless","usually","uttered","utterly","vacancy","variety","various","varying","venison","venting","venture","verdure","vicious","victory","viewing","village","violent", "visible","visited","visitor","waiting","walking","wanting","warmest","warrant","warwick","wasting","watched","watches","wavered","weakest","wearied","weather","wedding","weighed","weighty","welcome","welfare","whether","whisper","whither","wickham","william","willing","winding","windows","winking","wishing","without","witness","womanly", "wonders","worldly","wounded","writing","written","yawning","yielded","younger" }
    austin_words |= { "ablution","abruptly","absolute","abundant","acceding","accepted","accident","accosted","accounts","accuracy","accurate","accusing","acquaint","acquired","acrimony","activity","actually","actuated","addition","adequate","adhering","admiring","admitted","advanced","advances","advising","affected","affinity","afforded","agitated","agreeing", "alacrity","alarming","alighted","alliance","allowing","alluding","allusion","although","ambition","anecdote","animated","announce","answered","anything","anywhere","apparent","appeared","appeased","appetite","applying","approach","approved","archness","ardently","argument","arranged","arranges","arrested","arriving","arrogant","artfully", "articles","ascended","ashworth","asperity","assembly","assented","asserted","assisted","assuring","astonish","attached","attacked","attained","attended","attitude","attorney","audience","avoiding","awakened","backward","bakewell","banished","beatings","beauties","becoming","bedrooms","behavior","believed","believes","belonged","benefits", "bestowed","betrayed","bewailed","bingleys","bitterly","blenheim","blessing","blushing","boasting","bordered","borrowed","boundary","breaking","breathed","breeding","brighton","bringing","brooking","brothers","building","business","calmness","capacity","careless","caroline","carriage","carrying","catching","cautious","celerity","censured", "ceremony","changing","chaperon","charming","cheating","checking","cheerful","cheering","children","choosing","civility","clearing","clerical","coachman","coherent","coincide","coloured","combated","comforts","commerce","commonly","compared","complain","complete","complied","composed","comprise","conceals","conceive","concerns","concerto", "conclude","confined","confirms","confused","conjugal","conquest","consider","consists","consoled","constant","contains","contempt","contents","continue","contrary","contrast","contrive","converse","conveyed","convince","coquetry","coughing","counting","courtesy","courtier","courting","covering","creative","creature","critical","crossing", "crushing","cucumber","curricle","curtains","daughter","dazzling","deceived","deceives","deciding","decisive","declared","declares","declined","decorums","defended","deferred","defiance","delicacy","delicate","delights","departed","depended","deprived","deranged","derision","describe","deserted","deserved","deserves","designed","desiring", "desirous","despised","despises","destined","detached","detailed","detained","detected","detested","devoting","dialogue","dictated","dictates","diffused","dilatory","directed","directly","disclaim","disclose","discover","disgrace","disguise","disliked","dislikes","dispense","disposal","disposed","disputes","disquiet","dissuade","distance", "distress","distrust","diverted","dividing","domestic","doubtful","doubting","dovedale","draughts","drawings","dreadful","dreading","dressing","drinking","drooping","dullness","duration","dwelling","earliest","easiness","eclipsed","educated","efficacy","effusion","elegance","elevated","eligible","eloquent","embraced","eminence","emotions", "emphasis","emphatic","employed","enabling","encamped","endeared","enduring","enforced","engaging","enjoying","enormity","ensigncy","entailed","entering","entirely","entitled","entrance","entreaty","envelope","environs","equalled","equipage","escaping","esteemed","evenings","evenness","everyone","examined","exceeded","exciting","executed", "exercise","exerting","exertion","exigence","existing","expected","expedite","expences","expenses","explicit","exposing","exposure","extended","extorted","extracts","faithful","familiar","families","fancying","farewell","farthing","fashions","fastened","fatigued","favoured","fearless","feathers","features","february","feelings","felicity", "feverish","fighting","finances","finished","firmness","flirting","fluently","followed","forcibly","foreseen","foretold","forgiven","formerly","forsters","fortunes","forwards","fourthly","freckled","frequent","friendly","frighted","frighten","gaieties","gamester","gardener","gardiner","gathered","generous","gentlest","glancing","goodness", "goodwill","goulding","governed","graceful","gracious","grandeur","grateful","greatest","grieving","grievous","grossest","guardian","guidance","habitual","handsome","happened","happiest","hardened","hardship","hastened","hatfield","hazarded","headache","heartily","heedless","heighten","hesitate","hitherto","honestly","honoured","hopeless", "horrible","humanity","humbling","humility","humoured","hunsford","hurrying","husbands","idleness","ignorant","imagined","imitated","imparted","impelled","implicit","imposing","improper","improved","improves","impudent","impulses","impunity","imputing","incensed","inclined","included","increase","incurred","indebted","indirect","indolent", "indulged","infamous","inferior","infinite","informed","injuries","injuring","innocent","inquired","insisted","insolent","inspired","inspires","instance","instruct","insulted","intended","intently","interest","interval","intimacy","intimate","intruder","inviting","involved","involves","jealousy","journeys","joyfully","judgment","kindness", "ladyship","lamented","landlord","language","latterly","laudable","laughing","laughter","lawfully","learning","lessened","levelled","lifetime","likeness","likewise","listened","listener","lodgings","luckiest","luckless","luncheon","maintain","manifold","marriage","marrying","masterly","material","maternal","meanness","meantime","measures", "meditate","meetings","memories","messages","mildness","military","milliner","mingling","minutely","minutest","mischief","miseries","misleads","missking","misspope","mistaken","mistakes","mistress","mistrust","moderate","morality","moralize","moreover","mornings","mounting","mrbennet","mrmorris","mrsdarcy","mrshurst","mutually","narrowly", "nearness","neatness","needless","negative","nicholls","nightcap","nonsense","northern","nothings","noticing","november","nowadays","numerous","nuptials","objected","obliging","observed","observer","obtained","obtruded","occasion","occupied","occupies","occurred","oddities","offended","offenses","offering","officers","openness","operated", "opinions","opposite","ordained","ordinary","original","outlived","outstrip","overcame","overcome","overhear","overlook","overtook","parading","parental","partners","passages","passions","pathetic","patience","pavement","peculiar","pedantic","penitent","perceive","perforce","performs","persists","personal","persuade","perusing","perverse", "petition","phillips","pictured","pictures","pitiable","planning","pleasant","pleasing","pleasure","pointing","polished","politely","polluted","porridge","portrait","position","positive","possible","possibly","powerful","practice","preceded","precious","prefaced","premises","prepared","presence","presents","preserve","presided","pressing", "presumed","pretence","pretense","prettier","prevents","previous","probable","probably","proclaim","procured","produced","progress","promised","promises","promoted","prompted","properly","property","proposal","proposed","prospect","proudest","provided","provoked","prudence","publicly","punctual","purchase","pursuing","pursuits","pyramids", "quantity","quarters","question","quitting","ramsgate","rapacity","rapidity","raptures","rashness","rational","reaching","realised","reappear","recalled","received","reckoned","recovery","referred","refusals","refusing","regained","regarded","regiment","regulars","regulate","rejected","rejoiced","rejoined","relating","relation","relative", "reliance","relieved","relished","remained","remarked","remember","reminded","removing","rendered","renewing","repaired","repeated","repelled","repented","repining","replying","reproach","reproofs","repulsed","required","requited","research","resented","reserved","reserves","residing","resigned","resisted","resolute","resolved","resource", "respects","restless","restored","restrain","resuming","retained","returned","revealed","revolted","rewarded","reynolds","ridicule","rightful","romantic","rudeness","sagacity","sameness","sanction","sanguine","saturday","scarcely","scarcity","scheming","scolding","scotland","scrupled","scruples","scrutiny","secluded","seconded","secondly", "secretly","security","selected","sensible","sensibly","sentence","sentinel","separate","serenity","servants","services","settling","severest","severity","shameful","shifting","shocking","shopping","shrewish","silenced","silently","silliest","simpered","singling","singular","sisterly","situated","sixpence","sleeping","slighted","slightly", "smallest","smoothly","sneering","softened","softness","soldiers","solidity","solitary","solitude","somebody","somewhat","spacious","sparkled","speaking","speeches","speedily","spending","spiteful","splendid","sportive","sprained","standing","starting","startled","steadily","stepping","stirring","stopping","stranger","strength","strictly", "striking","striving","stronger","strongly","struggle","studious","studying","stupider","subjects","subsided","succeeds","suddenly","suffered","sufferer","suitable","summoned","superior","supplied","supposed","suppress","surmises","surmount","surprise","survived","survivor","suspects","suspense","sweetest","swelling","syllable","symmetry", "symptoms","taciturn","teaching","tempered","tendency","tenderly","terrific","thankful","thanking","theatres","thinking","thirteen","thorough","thoughts","thousand","throwing","thursday","thwarted","tiresome","together","toilette","tortured","tranquil","treasure","treating","trembled","trespass","trifling","trimming","trusting","unabated", "unallied","uncommon","unfolded","unjustly","unlikely","unmarked","unseldom","unshaken","unsocial","untitled","unworthy","upstairs","valuable","vanished","variance","ventured","veracity","vexation","vicinity","violated","violence","visiting","visitors","vivacity","wandered","wantonly","watchful","watching","wavering","weakened","weakness", "welcomed","whatever","whenever","wherever","wilfully","windings","withdrew","withheld","wondered","wounding","wretched","yielding","youngest","yourself" }
    austin_words |= { "abatement","abhorrent","abilities","abominate","absurdity","accepting","accompany","according","accounted","achieving","acquiesce","additions","addressed","addresses","adjusting","admirable","admission","admitting","adoration","advantage","adventure","advisable","affection","afflicted","affording","affronted","afternoon","agitation", "agreeable","agreeably","agreement","alienated","alleviate","allowable","allowance","allusions","alternate","amazement","amendment","amounting","amusement","anecdotes","animating","animation","announced","answering","anxiously","apartment","apologies","apologise","appearing","appertain","appointed","arguments","arranging","arrogance", "ascertain","assembled","asserting","assertion","assiduous","assistant","assisting","assurance","atonement","attempted","attendant","attending","attention","attentive","attracted","attribute","augmented","austerity","authorise","authority","avoidance","backwards","barbarous","barefaced","beauteous","beautiful","beginning","behaviour", "beholding","believing","belonging","benefited","bestowing","bewitched","bitterest","blameable","blameless","bordering","boundless","bracelets","breakfast","breathing","brightest","brotherly","calculate","cambridge","canvassed","captivate","carefully","carriages","catherine","ceaseless","censuring","certainly","certainty","cessation", "challenge","character","charlotte","cheapside","cherished","chestnuts","childhood","christian","christmas","clamorous","clergyman","coincided","collected","collinses","colouring","comforted","commanded","commended","commonest","companion","comparing","complaint","completed","complying","composure","comprised","concealed","conceited", "concerned","concisely","concluded","condemned","condition","conducted","confessed","confident","confiding","confirmed","confusion","congenial","connected","connubial","conquered","conscious","consented","consigned","consisted","consoling","constancy","construed","consulted","contained","contented","continual","continued","contrived", "conversed","conveying","convinced","cordially","cottagers","courteous","courtship","creatures","creditors","criticise","curiosity","curtailed","curtseyed","dangerous","daughters","decamping","deceitful","deceiving","deception","decidedly","decisions","declaring","defection","defective","deference","deficient","dejection","delicious", "delighted","delivered","demanding","departure","dependent","depending","depravity","depressed","descended","described","desertion","deserving","designing","desirable","despaired","desperate","despising","destitute","destroyed","detaching","detaining","detection","determine","dictating","different","difficult","diffident","dignified", "diligence","directing","direction","discharge","disclosed","discourse","discovery","discredit","discussed","disdained","disgraced","disgusted","dishonest","disliking","dismissed","displayed","displease","disposing","dissemble","dissolved","dissuaded","disturbed","diversion","domestics","doubtless","ductility","duplicity","dutifully", "eagerness","earnestly","eccentric","education","effectual","effusions","elevating","elevation","elizabeth","elopement","eloquence","elsewhere","embracing","emergence","employing","emptiness","encounter","encourage","endeavour","endurable","energetic","engrossed","enjoyment","enlarging","entailing","entertain","entreated","equivocal", "essential","establish","estimable","estimated","etiquette","everybody","evidently","examining","exceeding","excellent","excepting","exception","excessive","exchanged","exclaimed","exclusion","execution","executors","exhausted","existence","expecting","expedient","explained","expressed","expressly","exquisite","extensive","extremely", "exuberant","eyelashes","faculties","falsehood","farmhouse","faultless","favourite","feelingly","fervently","fingering","finishing","fireplace","flattered","fluttered","following","footstool","forfeited","forgiving","forgotten","formality","formation","fortitude","fortnight","fortunate","forwarded","forwarder","foxhounds","frankness", "fretfully","frivolous","fugitives","furnished","furniture","gallantry","gardiners","gathering","generally","gentleman","gentlemen","georgiana","giddiness","godfather","gossiping","gouldings","governess","gradually","gratified","gratitude","greatness","grosvenor","guardians","hackneyed","handsomer","happening","happiness","harboured", "hardships","hastening","hatefully","healthful","heartfelt","hereafter","hermitage","hesitated","highflown","histories","horseback","household","housemaid","howsoever","hypocrisy","hysterics","ignorance","illiberal","imaginary","imitation","immediate","immovable","impartial","impatient","impetuous","impolitic","important","importing", "importune","impressed","imprudent","impudence","incapable","incessant","including","increased","increases","incumbent","indecorum","indicated","indignant","indignity","indolence","indulgent","indulging","inflicted","influence","informing","ingenious","ingenuity","inherited","injurious","injustice","innocence","inquiries","inquiring", "insincere","insolence","inspiring","instances","instantly","insulting","integrity","intending","intention","interfere","interpose","interrupt","intervals","intervene","interview","intimates","intricate","intrigues","introduce","intruding","intrusion","inventing","invention","involving","irritable","irritated","jestingly","judgement", "justified","knowledge","lamenting","languages","leisurely","lessening","liberally","liberties","lightness","lingering","listening","liveliest","liverpool","longbourn","loveliest","magnitude","malicious","manoeuvre","matrimony","mayoralty","meanwhile","meditated","mentioned","mercenary","mischance","miserable","miserably","missdarcy", "misseliza","misslizzy","misslucas","misslydia","misswebbs","momentary","mortified","mortifies","mountains","mrbingley","mrcollins","mrphillip","mrsbennet","mrsyounge","mrwickham","multitude","narrative","narrowest","naturally","necessary","necessity","negatived","neglected","negligent","neighbour","newcastle","newcomers","newspaper", "nominally","northward","nourishes","obeisance","objecting","objection","observing","obstacles","obstinacy","obstinate","occasions","occurring","offending","offensive","officious","oppressed","originate","ornaments","otherwise","ourselves","overflows","overheard","overjoyed","overpower","overruled","overtaken","overthrow","overtures", "painfully","paintings","palatable","panegyric","parsonage","patronage","patroness","pecuniary","pemberley","perceived","perfectly","performed","performer","permanent","permitted","perpetual","persisted","personage","persuaded","perturbed","petrified","petticoat","petulance","pleasures","plentiful","pointedly","pollution","portraits", "positions","possessed","possesses","possessor","posterity","postponed","powdering","practised","practises","preaching","preceding","precisely","precision","preferred","prejudice","preparing","presented","presently","preserved","presuming","pretended","prettiest","prettyish","prevailed","prevented","principal","principle","privately", "privilege","proceeded","procuring","professed","profusion","projected","promising","pronounce","proposals","propriety","prospects","protested","providing","provision","provoking","purchased","purchases","purposely","quadrille","qualified","qualities","quarreled","quartered","querulous","questions","quickness","rapturous","readiness", "realities","reasoning","receiving","reception","recollect","recommend","reconcile","recovered","rectitude","recurring","reference","reflected","refrained","regarding","regretted","regularly","regulated","rejecting","rejection","rejoicing","relations","reluctant","remainder","remaining","reminding","rencontre","rendering","repeating", "repinings","reporting","represent","repressed","repugnant","repulsive","requested","requester","requiring","requisite","resentful","residence","resigning","resisting","resolving","respected","restoring","restraint","retailing","retaining","retaliate","retreated","returning","revealing","revenging","reverting","revolving","sacrifice", "sarcastic","satirical","satisfied","scattered","searching","seclusion","seconding","seduction","selecting","seniority","sensation","sentences","sentiment","separated","separates","september","seriously","servility","shameless","sharpened","sheltered","shillings","shortness","shoulders","shrubbery","sideboard","simpleton","sincerely", "sincerity","situation","sleepless","slightest","smilingly","societies","solemnity","something","sometimes","somewhere","speediest","splendour","spokesman","sportsmen","spreading","springing","squeamish","stability","staggered","staircase","statement","stationed","steadfast","stiffness","stockings","strangely","strangers","stretched", "strictest","strongest","struggled","struggles","stumbling","stupidity","submitted","subsisted","substance","succeeded","successor","suffering","suggested","supplying","supported","supposing","surprised","surveying","suspected","suspended","suspicion","sustained","swallowed","sweetness","syllables","temporary","testified","testimony", "therefore","thereupon","tolerable","tolerably","tractable","tradesman","transient","transport","travelled","treasured","treatment","trembling","troubling","turnpikes","unabashed","unalloyed","unbending","uncertain","unchanged","unconcern","undeceive","undecided","undergone","undoubted","undutiful","unequally","unfeeling","unfolding", "unguarded","unhappily","uniformly","universal","unluckily","unnatural","unreserve","unsettled","unstudied","unsubdued","untouched","unvarying","unwelcome","unwilling","upbraided","uppermost","uselessly","valueless","variation","varieties","vehemence","venturing","vestibule","vexations","vexatious","violation","violently","voluntary", "vulgarity","wandering","wearisome","wednesday","welcoming","westerham","whichever","whimsical","whispered","wickedest","willfully","willingly","withdrawn","withstood","witnessed","wonderful","wondering","worthless","yesterday" }
    austin_words |= { "abhorrence","abominable","abominably","abruptness","absolutely","abundantly","acceptable","acceptance","accidental","accounting","accusation","accustomed","acquainted","additional","addressing","admiration","admittance","advantages","advertised","affability","affections","afflicting","affliction","afterwards","agitations","alleviated", "allowances","alteration","altogether","amusements","answerable","antagonist","anticipate","apartments","apologised","apothecary","apparently","appearance","approached","archbishop","artificial","assemblies","assertions","assistance","assurances","astonished","attachment","attempting","attendance","attendants","attentions","attraction", "attributed","authorised","authorized","backgammon","beforehand","befriended","beneficial","benefiting","benevolent","bequeathed","bewildered","bewitching","birmingham","bitterness","breathless","bridegroom","brightened","brilliancy","calculated","captivated","cautioning","celebrated","ceremonies","characters","charmingly","chatsworth", "cheerfully","circulated","civilities","coarseness","collecting","collection","commission","companions","comparison","compassion","compatible","complained","complaints","completely","completion","complexion","compliance","compliment","composedly","comprehend","concealing","conception","concerning","conciliate","concluding","conclusion", "condescend","conditions","condolence","conference","confession","confidante","confidence","confirming","conjecture","connection","connivance","conscience","consenting","consequent","considered","consistent","constantly","constitute","construing","consulting","containing","continuing","contracted","contradict","contrasted","contribute", "convenient","conversing","converting","conviction","cordiality","correspond","corruption","counteract","creditable","creditably","criticisms","deficiency","definition","degenerate","delightful","delighting","delivering","dependence","deportment","depreciate","derbyshire","descending","describing","deservedly","designedly","despicable", "despicably","desponding","determined","detestable","difference","difficulty","diffidence","dimensions","diminution","directions","disappoint","disapprove","discerning","discharged","disclaimed","disclosure","discompose","discourage","discourses","discovered","discretion","discussion","disengaged","disgracing","disgusting","dishonesty", "dismission","dispatched","dispelling","dispirited","displaying","displeased","disputable","disrespect","disservice","distracted","distressed","distribute","distrusted","disturbers","doubtingly","downstairs","dreadfully","eastbourne","employment","encouraged","endeavours","engagement","engrossing","enjoyments","entreaties","entreating", "equivalent","especially","essentials","estimation","everything","everywhere","exaggerate","exasperate","excellence","excellency","exclaiming","exercising","exhibiting","exhibition","experience","explaining","explicitly","expressing","expression","expressive","exuberance","exultation","faithfully","familiarly","fastidious","favourable", "favourably","favourites","flattering","flirtation","forbearing","forbidding","forgetting","formidable","forwarding","foundation","frequently","friendless","friendlier","friendship","frightened","generality","generation","generously","gentleness","gracefully","graciously","gratefully","gratifying","grievances","grievously","groundwork", "haggerston","handsomely","handsomest","headstrong","heartening","heightened","henceforth","hereabouts","heretofore","hesitating","hesitation","honourable","horsewoman","housemaids","illiterate","imaginable","imitations","impassable","impatience","implacable","importance","importuned","impossible","impressing","impression","impressive", "improbable","imprudence","impurities","inadequate","incivility","increasing","incredible","indecision","indefinite","indelicacy","indelicate","indiscreet","indisposed","individual","inducement","indulgence","inevitable","inevitably","inferences","infinitely","inflexibly","infliction","influenced","inheriting","inhumanity","iniquitous", "injunction","innocently","insensible","insipidity","inspection","instituted","instructed","instrument","intentions","interested","intimately","intimation","intimidate","introduced","invaluable","invariable","invariably","invectives","invitation","irritation","justifying","kenilworth","knighthood","laughingly","liberality","lieutenant", "likelihood","liveliness","loveliness","magistrate","maintained","management","materially","mediocrity","meditating","meditation","melancholy","mentioning","michaelmas","miniatures","minuteness","miraculous","misconduct","misfortune","misleading","missbennet","misswatson","moderation","monotonous","mortifying","mrgardiner","mrphillips", "mrrobinson","mrsbingley","mrscollins","mrsforster","mrswickham","nectarines","needlessly","needlework","neglecting","negligence","neighbours","northwards","objections","obligation","obligingly","obsequious","occasional","occasioned","occupation","opposition","ordination","originally","originated","overcoming","overlooked","overspread", "overthrown","palliation","partiality","particular","partridges","peculiarly","perceiving","performers","permission","perplexity","persevered","persisting","personages","persuasion","petitioned","phillipses","philosophy","physicians","pianoforte","plantation","pleasanter","pleasantly","pleasantry","politeness","popularity","positively", "possessing","possession","postilions","postscript","practising","precluding","preference","preferment","prejudiced","prejudices","pressingly","pretending","pretension","prevailing","previously","principles","privileged","proceeding","prodigious","productive","professing","profession","proficient","profligacy","profligate","prohibited", "pronounced","propitious","proportion","proprietor","prosperity","prosperous","protection","protesting","prudential","punctually","punishment","quarreling","questioned","rationally","reanimated","reasonable","reasonably","recognized","reconciled","recovering","recreation","reflecting","reflection","refreshing","regardless","regretting", "regulation","relinquish","reluctance","remarkable","remarkably","remembered","repeatedly","repentance","repetition","repressing","reproached","reproaches","repugnance","reputation","requesting","resentment","resistance","resolutely","resolution","resounding","respectful","respecting","respective","restrained","retirement","retreating", "revolution","ridiculing","ridiculous","sacrificed","salutation","sanctioned","satisfying","scampering","scandalous","seasonable","sedateness","seminaries","sensations","sentiments","separately","separating","separation","settlement","similarity","soliciting","solicitude","spiritless","steadiness","stratagems","stretching","strictures", "strikingly","struggling","subjection","subsequent","subsisting","substitute","succeeding","successful","succession","suddenness","sufferings","sufficient","suggesting","suggestion","superseded","suppressed","surpassing","surrounded","suspecting","suspicions","suspicious","sympathise","temptation","tenderness","testifying","thankfully", "thebennets","themselves","thoroughly","thoughtful","threadbare","threatened","throughout","tormenting","tranquilly","transition","transpired","transports","travellers","travelling","tremblings","triumphant","triumphing","ultimately","unaffected","unassailed","unassuming","unattended","unavailing","unbecoming","uncommonly","understand", "understood","undertaken","undeserved","uneasiness","unexampled","unexpected","ungenerous","ungracious","uniformity","unkindness","unpleasant","unpleasing","unprepared","unreserved","unshackled","unsuitable","unwearying","unworthily","upbraiding","veneration","vigorously","villainous","volatility","volubility","vouchsafed","warehouses", "weaknesses","whispering","wickedness","wilderness","witnessing","witticisms","wretchedly","yourselves" }
    austin_words |= { "absurdities","accompanied","accordingly","accusations","acknowledge","acquainting","acquisition","advancement","affectation","affirmative","allurements","alterations","alternative","anticipated","apologising","appearances","application","appointment","apprehended","approaching","approbation","arrangement","assiduously","associating", "attachments","attentively","attractions","attributing","authorising","awkwardness","barbarously","beneficence","benevolence","breakfasted","brightening","calculation","captivating","captivation","ceremonious","chambermaid","christening","circulating","circulation","circumspect","coincidence","comfortable","comfortably","comfortless", "commendable","communicate","comparative","comparisons","competition","complacency","complaining","complaisant","compliments","composition","comprehends","compromised","concealment","concurrence","condescends","conditional","confederacy","confidently","confinement","conjectured","conjectures","conjunction","connections","consequence", "considering","consistency","consolation","consolatory","constrained","contentment","continually","continuance","contrariety","contributed","contrivance","convenience","conversible","countenance","counterpart","cultivation","curiosities","declaration","degradation","deliberated","denominated","description","desperation","destructive", "determining","development","dictatorial","differences","differently","diffuseness","digressions","discernible","discernment","discharging","discomposed","discouraged","discovering","disgraceful","disinclined","disobliging","displeasure","disposition","disregarded","dissipation","distinction","distinguish","distraction","distressing", "disturbance","diversified","earnestness","effectually","eligibility","embarrassed","employments","encouraging","encroaching","encumbrance","endeavoured","engagements","entertained","enumerating","enumeration","established","examination","exceedingly","exceptional","excessively","exclamation","expectation","experienced","explanation", "explanatory","expressions","extenuating","extractions","extravagant","familiarity","fashionable","fitzwilliam","fluctuating","flutterings","forbearance","forgiveness","fortunately","foundations","fretfulness","generations","gentlewoman","gracechurch","grandfather","handwriting","harringtons","hospitality","housekeeper","humiliating", "humiliation","illustrious","imagination","immediately","impatiently","imperfectly","impertinent","impropriety","improvement","inattention","inattentive","incessantly","inclination","incredulity","incredulous","independent","indifferent","indignation","inducements","ineffectual","infatuation","inferiority","influencing","informality", "information","ingratitude","inhabitants","injunctions","inoffensive","insinuating","instability","instructing","instruction","intelligent","intercourse","interesting","interfering","interrupted","intimidated","intolerable","intrepidity","introducing","invitations","involuntary","irreligious","irrevocably","maintaining","mantelpiece", "matrimonial","meditations","misfortunes","missbennets","missbingley","misslucases","mrsannesley","mrsgardiner","mrsnicholls","mrsphillips","mrsreynolds","necessarily","netherfield","nonsensical","nothingness","obligations","observances","observation","occurrences","opportunity","ostentation","outstripped","overbearing","overflowing", "overpowered","particulars","peculiarity","penetration","perceptible","perfections","performance","perpetually","persevering","persuasions","philosopher","philosophic","picturesque","playfulness","pleasantest","possibility","precipitate","predominate","preparation","presumption","pretensions","principally","probability","proceedings", "professions","proficiency","prognostics","pronouncing","proportions","punctuality","quarrelling","quarrelsome","rapturously","recognizing","recollected","recommenced","recommended","reconciling","refinements","reflections","refreshment","regimentals","remembering","remembrance","represented","resemblance","resentfully","resentments", "troublesome","twelvemonth","unalterable","unavoidable","unavoidably","unblemished","uncertainty","unconcerned","unconnected","undertaking","undervalued","undeserving","undoubtedly","unforgiving","unfortunate","unhappiness","unimportant","universally","unknowingly","unnaturally","unnecessary","unprotected","unqualified","untinctured", "resignation","respectable","restoration","scarborough","selfishness","sensibility","serviceable","settlements","significant","slightingly","speculation","stateliness","steadfastly","strangeness","strenuously","substantial","superiority","supposition","surrounding","temptations","termination","thoughtless","transferred","trepidation", "unwillingly","vindication","voluntarily","willingness","withdrawing","wonderfully" }
    austin_words |= { "accidentally","accompanying","accomplished","acknowledged","acquaintance","acquiescence","advantageous","affectionate","anticipating","anticipation","apprehending","apprehension","apprehensive","arrangements","ascertaining","astonishment","boisterously","carelessness","cautiousness","chamberlayne","characterise","cheerfulness","circumstance","commencement","commendation","commissioned","communicated","compensation","complaisance","complimented","comprehended","conciliating","conciliatory","condescended","confidential","confirmation","congratulate","conjecturing","consequently","considerable","considerably","constitution","construction","contradicted","contrariwise","controverted","conversation","corroborated","counteracted","deliberately","deliberation","delightfully","disadvantage","disagreeable","disagreeably","disagreement","disappointed","disconcerted","discontented","disheartened","dishonorable","dispositions","dissatisfied","distractedly","economically","emphatically","endeavouring","exaggeration","exclamations","expectations","explanations","expressively","extinguished","extravagance","graciousness","guardianship","handkerchief","headquarters","housekeeping","hypocritical","illustration","imaginations","impartiality","impenetrably","imperfection","impertinence","implicitness","improvements","incautiously","inclinations","inconvenient","independence","indifference","indistinctly","individually","instructions","insufferable","insufferably","insufficient","intelligence","intelligible","interference","intermediate","intermission","interrupting","interruption","introduction","irremediable","lamentations","mechanically","missdebourgh","missgrantley","monosyllable","neighbouring","observations","occasionally","oppressively","ostentatious","overhearings","overpowering","overthrowing","parishioners","particularly","perseverance","perturbation","perverseness","pleasantness","precipitance","predominance","premeditated","preparations","prepossessed","presentation","preservation","preservative","prodigiously","propensities","proportioned","provocations","recollecting","recollection","recommending","relationship","remonstrance","representing","satisfaction","satisfactory","solicitation","stubbornness","successfully","successively","sufficiently","suitableness","supercilious","superintends","supplication","suppositions","synonymously","thankfulness","transactions","triumphantly","unacquainted","unaffectedly","unanswerable","uncontrolled","undervaluing","undetermined","undiminished","unexpectedly","unfavourable","unfavourably","unfrequently","ungovernable","universities","unpardonable","unpleasantly","unpretending","unprincipled","unprofitable","unreasonable","unreasonably","unrestrained","unsuspicious","watchfulness","wretchedness" }
    # GitHub 5 Letter Words
    austin_words |= { "aargh" , "abaca" , "abaci" , "aback" , "abaft" , "abase" , "abash" , "abate" , "abbey" , "abbot" , "abeam" , "abend" , "abets" , "abhor" , "abide" , "abled" , "abler" , "abode" , "abort" , "about" , "above" , "absit" , "abuse" , "abuts" , "abuzz" , "abyss" , "ached" , "aches" , "achoo" , "acids" , "acing" , "acked" , "acmes" , "acned" , "acnes" , "acorn" , "acres" , "acrid" , "acted" , "actin" , "actor" , "acute" , "adage" , "adapt" , "added" , "adder" , "addle" , "adept" , "adieu" , "adios" , "adlib" , "adman" , "admen" , "admit" , "admix" , "adobe" , "adopt" , "adore" , "adorn" , "adult" , "adzes" , "aegis" , "aerie" , "affix" , "afire" , "afoot" , "afore" , "afoul" , "after" , "again" , "agape" , "agars" , "agate" , "agave" , "agent" , "agile" , "aging" , "agley" , "aglow" , "agone" , "agony" , "agora" , "agree" , "agues" , "ahead" , "ahhhh" , "ahold" , "ahoys" , "aided" , "aider" , "aides" , "ailed" , "aimed" , "aimer" , "aioli" , "aired" , "airer" , "aisle" , "aitch" , "ajuga" , "alack" , "alarm" , "album" , "alder" , "aleck" , "aleph" , "alert" , "algae" , "algal" , "algin" , "alias" , "alibi" , "alien" , "align" , "alike" , "alive" , "alkyd" , "alkyl" , "allay" , "alley" , "allot" , "allow" , "alloy" , "aloes" , "aloft" , "aloha" , "alone" , "along" , "aloof" , "aloud" , "alpha" , "altar" , "alter" , "altho" , "altos" , "alums" , "alway" , "amahs" , "amass" , "amaze" , "amber" , "ambit" , "amble" , "ameba" , "amend" , "amens" , "amide" , "amigo" , "amine" , "amino" , "amiss" , "amity" , "ammos" , "among" , "amour" , "amped" , "ample" , "amply" , "amuck" , "amuse" , "amyls" , "anded" , "anent" , "angel" , "anger" , "angle" , "angry" , "angst" , "anile" , "anima" , "anion" , "anise" , "ankhs" , "ankle" , "annas" , "annex" , "annoy" , "annul" , "annum" , "anode" , "anole" , "anted" , "antes" , "antic" , "antis" , "antsy" , "anvil" , "aorta" , "apace" , "apart" , "apers" , "aphid" , "aphis" , "apian" , "aping" , "apish" , "apnea" , "aport" , "apple" , "apply" , "apron" , "apses" , "apsos" , "aptly" , "aquae" , "aquas" , "arbor" , "arced" , "ardor" , "areal" , "areas" , "arena" , "argon" , "argot" , "argue" , "arias" , "arise" , "arity" , "armed" , "armor" , "aroma" , "arose" , "arras" , "array" , "arrow" , "arses" , "arson" , "artsy" , "arums" , "asana" , "ascot" , "ashen" , "ashes" , "aside" , "asked" , "asker" , "askew" , "aspen" , "aspic" , "assai" , "assay" , "assed" , "asses" , "asset" , "aster" , "astir" , "astro" , "atilt" , "atlas" , "atoll" , "atoms" , "atone" , "atria" , "attar" , "attic" , "audio" , "audit" , "auger" , "aught" , "augur" , "aunts" , "aurae" , "aural" , "auras" , "auric" , "autos" , "avail" , "avant" , "avast" , "avers" , "avert" , "avian" , "avoid" , "avows" , "await" , "awake" , "award" , "aware" , "awash" , "aways" , "awful" , "awing" , "awoke" , "axels" , "axial" , "axing" , "axiom" , "axled" , "axles" , "axman" , "axmen" , "axons" , "ayins" , "azine" , "azoic" , "azure" , "babel" , "babes" , "backs" , "bacon" , "baddy" , "badge" , "badly" , "bagel" , "baggy" , "bahts" , "bails" , "bairn" , "baits" , "baize" , "baked" , "baker" , "bakes" , "balds" , "baldy" , "baled" , "baler" , "bales" , "balks" , "balky" , "balls" , "bally" , "balms" , "balmy" , "balsa" , "banal" , "bands" , "bandy" , "banes" , "bangs" , "banjo" , "banks" , "banns" , "barbs" , "bards" , "bared" , "barer" , "bares" , "barfs" , "barfy" , "barge" , "baric" , "barks" , "barky" , "barms" , "barmy" , "barns" , "baron" , "basal" , "based" , "baser" , "bases" , "basic" , "basil" , "basin" , "basis" , "basks" , "bassi" , "basso" , "baste" , "batch" , "bated" , "bates" , "bathe" , "baths" , "batik" , "baton" , "batty" , "bauds" , "baulk" , "bawdy" , "bawls" , "bayed" , "bayou" , "bazar" , "beach" , "beads" , "beady" , "beaks" , "beaky" , "beams" , "beamy" , "beano" , "beans" , "beard" , "bears" , "beast" , "beats" , "beaus" , "beaut" , "beaux" , "bebop" , "bebug" , "becks" , "bedew" , "bedim" , "beech" , "beefs" , "beefy" , "beeps" , "beers" , "beery" , "beets" , "befit" , "befog" , "began" , "begat" , "beget" , "begin" , "begot" , "begun" , "beige" , "being" , "belay" , "belch" , "belie" , "belle" , "belli" , "bells" , "belly" , "below" , "belts" , "bench" , "bends" , "bents" , "beret" , "bergs" , "berms" , "berry" , "berth" , "beryl" , "beset" , "besot" , "bests" , "betas" , "betel" , "beths" , "bevel" , "bezel" , "bhang" , "bhoys" , "bibbs" , "bible" , "biddy" , "bided" , "bider" , "bides" , "bidet" , "biers" , "biffs" , "biffy" , "biggy" , "bight" , "bigly" , "bigot" , "biked" , "biker" , "bikes" , "biles" , "bilge" , "bilgy" , "bilks" , "bills" , "billy" , "bimbo" , "binds" , "binge" , "bingo" , "biome" , "biped" , "bipod" , "birch" , "birds" , "birth" , "bison" , "bitch" , "biter" , "bites" , "bitsy" , "bitty" , "blabs" , "black" , "blade" , "blahs" , "blame" , "bland" , "blank" , "blare" , "blash" , "blast" , "blats" , "blaze" , "bleak" , "blear" , "bleat" , "blebs" , "bleed" , "blend" , "bless" , "blest" , "blimp" , "blind" , "blini" , "blink" , "blips" , "bliss" , "blitz" , "bloat" , "blobs" , "block" , "blocs" , "bloke" , "blond" , "blood" , "bloom" , "blots" , "blown" , "blows" , "blowy" , "blued" , "bluer" , "blues" , "bluff" , "blunt" , "blurb" , "blurs" , "blurt" , "blush" , "board" , "boars" , "boast" , "boats" , "bobby" , "bocce" , "bocci" , "bocks" , "boded" , "bodes" , "bodge" , "boffo" , "boffs" , "bogey" , "boggy" , "bogie" , "bogus" , "boils" , "bolas" , "bolls" , "bolos" , "bolts" , "bombe" , "bombs" , "bonds" , "boned" , "boner" , "bones" , "bongo" , "bongs" , "bonks" , "bonne" , "bonny" , "bonus" , "boobs" , "booby" , "booed" , "books" , "booky" , "booms" , "boomy" , "boons" , "boors" , "boost" , "booth" , "boots" , "booty" , "booze" , "boozy" , "borax" , "bored" , "borer" , "bores" , "boric" , "borne" , "boron" , "bosky" , "bosom" , "boson" , "bossa" , "bossy" , "bosun" , "botch" , "bough" , "boule" , "bound" , "bouts" , "bowed" , "bowel" , "bower" , "bowie" , "bowls" , "boxed" , "boxer" , "boxes" , "bozos" , "brace" , "brack" , "bract" , "brads" , "braes" , "brags" , "braid" , "brain" , "brake" , "brand" , "brans" , "brant" , "brash" , "brass" , "brats" , "brava" , "brave" , "bravo" , "brawl" , "brawn" , "brays" , "braze" , "bread" , "break" , "bream" , "breed" , "brent" , "breve" , "brews" , "briar" , "bribe" , "brick" , "bride" , "brief" , "brier" , "bries" , "brigs" , "brims" , "brine" , "bring" , "brink" , "briny" , "brisk" , "broad" , "broil" , "broke" , "bromo" , "bronc" , "bronx" , "brood" , "brook" , "broom" , "broth" , "brown" , "brows" , "bruin" , "bruit" , "brung" , "brunt" , "brush" , "brusk" , "brute" , "bubba" , "bucks" , "buddy" , "budge" , "buena" , "bueno" , "buffa" , "buffo" , "buffs" , "buggy" , "bugle" , "build" , "built" , "bulbs" , "bulge" , "bulgy" , "bulks" , "bulky" , "bulls" , "bully" , "bumph" , "bumps" , "bumpy" , "bunch" , "bunco" , "bunds" , "bungs" , "bunko" , "bunks" , "bunny" , "bunts" , "buoys" , "buret" , "burgs" , "burls" , "burly" , "burns" , "burnt" , "burps" , "burro" , "burrs" , "burry" , "burst" , "busby" , "bused" , "buses" , "bushy" , "busks" , "busts" , "busty" , "butch" , "butte" , "butts" , "butyl" , "buxom" , "buyer" , "buzzy" , "bwana" , "bylaw" , "byres" , "bytes" , "byway" , "cabal" , "cabby" , "cabin" , "cable" , "cacao" , "cache" , "cacti" , "caddy" , "cadet" , "cadge" , "cadre" , "cafes" , "caged" , "cager" , "cages" , "cagey" , "cairn" , "caked" , "cakes" , "calix" , "calks" , "calla" , "calls" , "calms" , "calve" , "calyx" , "camel" , "cameo" , "campo" , "camps" , "campy" , "canal" , "candy" , "caned" , "caner" , "canes" , "canna" , "canny" , "canoe" , "canon" , "canst" , "canto" , "cants" , "caped" , "caper" , "capes" , "capon" , "capos" , "carat" , "cards" , "cared" , "carer" , "cares" , "caret" , "cargo" , "carne" , "carny" , "carob" , "carol" , "carom" , "caron" , "carps" , "carpy" , "carry" , "carte" , "carts" , "carve" , "casas" , "cased" , "cases" , "casks" , "caste" , "casts" , "casus" , "catch" , "cater" , "catty" , "caulk" , "cauls" , "cause" , "caved" , "caves" , "cavil" , "cawed" , "cease" , "cedar" , "ceded" , "ceder" , "cedes" , "ceils" , "celeb" , "cello" , "cells" , "cento" , "cents" , "chafe" , "chaff" , "chain" , "chair" , "chalk" , "champ" , "chant" , "chaos" , "chaps" , "chard" , "charm" , "chars" , "chart" , "chary" , "chase" , "chasm" , "chats" , "chaws" , "cheap" , "cheat" , "check" , "cheek" , "cheep" , "cheer" , "chefs" , "chert" , "chess" , "chest" , "chews" , "chewy" , "chick" , "chide" , "chief" , "chiff" , "child" , "chile" , "chili" , "chill" , "chime" , "chimp" , "china" , "chine" , "chink" , "chino" , "chins" , "chips" , "chirp" , "chits" , "chive" , "chock" , "choir" , "choke" , "chomp" , "choos" , "chops" , "chord" , "chore" , "chose" , "chows" , "chuck" , "chuff" , "chugs" , "chump" , "chums" , "chunk" , "churl" , "churn" , "chute" , "cider" , "cigar" , "cilia" , "cills" , "cinch" , "circa" , "cirri" , "cited" , "cites" , "civet" , "civic" , "civil" , "civvy" , "clack" , "clads" , "claim" , "clamp" , "clams" , "clang" , "clank" , "clans" , "claps" , "clash" , "clasp" , "class" , "clave" , "claws" , "clays" , "clean" , "clear" , "cleat" , "clefs" , "cleft" , "clerk" , "clews" , "click" , "cliff" , "climb" , "clime" , "cling" , "clink" , "clips" , "cloak" , "clock" , "clods" , "clogs" , "clomp" , "clone" , "clops" , "close" , "cloth" , "clots" , "cloud" , "clout" , "clove" , "clown" , "cloys" , "clubs" , "cluck" , "clued" , "clues" , "clump" , "clung" , "clunk" , "coach" , "coals" , "coast" , "coati" , "coats" , "cobra" , "cocas" , "cocci" , "cocks" , "cocky" , "cocoa" , "cocos" , "codas" , "coded" , "coder" , "codes" , "codex" , "codon" , "coeds" , "cohos" , "coifs" , "coils" , "coins" , "coked" , "cokes" , "colas" , "colds" , "colic" , "colon" , "color" , "colts" , "comas" , "combo" , "combs" , "comer" , "comes" , "comet" , "comfy" , "comic" , "comma" , "comps" , "conch" }
    austin_words |= { "condo" , "coned" , "cones" , "coney" , "conga" , "conic" , "conks" , "cooch" , "cooed" , "cooks" , "cooky" , "cools" , "coops" , "coots" , "coped" , "coper" , "copes" , "copra" , "copse" , "coqui" , "coral" , "cords" , "cordy" , "cored" , "corer" , "cores" , "corgi" , "corks" , "corky" , "corms" , "corns" , "cornu" , "corny" , "corps" , "coset" , "costa" , "costs" , "cotes" , "cotta" , "couch" , "cough" , "could" , "count" , "coupe" , "coups" , "court" , "couth" , "coven" , "cover" , "coves" , "covet" , "covey" , "cowed" , "cower" , "cowls" , "cowry" , "coxed" , "coxes" , "coyer" , "coyly" , "coypu" , "cozen" , "crabs" , "crack" , "craft" , "crags" , "cramp" , "crams" , "crane" , "crank" , "craps" , "crash" , "crass" , "crate" , "crave" , "crawl" , "craws" , "craze" , "crazy" , "creak" , "cream" , "credo" , "creed" , "creek" , "creel" , "creep" , "creme" , "crepe" , "crept" , "cress" , "crest" , "crews" , "cribs" , "crick" , "cried" , "crier" , "cries" , "crime" , "crimp" , "crink" , "crisp" , "crits" , "croak" , "crock" , "crocs" , "croft" , "crone" , "crony" , "crook" , "croon" , "crops" , "cross" , "croup" , "crowd" , "crown" , "crows" , "crude" , "cruds" , "cruel" , "cruet" , "cruft" , "crumb" , "crump" , "cruse" , "crush" , "crust" , "crypt" , "cubby" , "cubed" , "cuber" , "cubes" , "cubic" , "cubit" , "cuffs" , "cuing" , "cukes" , "culls" , "culpa" , "cults" , "cumin" , "cunts" , "cupid" , "cuppa" , "cuppy" , "curbs" , "curds" , "curdy" , "cured" , "curer" , "cures" , "curia" , "curie" , "curio" , "curls" , "curly" , "curry" , "curse" , "curve" , "curvy" , "cushy" , "cusps" , "cuspy" , "cuter" , "cutie" , "cutup" , "cycad" , "cycle" , "cynic" , "cysts" , "czars" , "dacha" , "daddy" , "dados" , "daffy" , "daily" , "dairy" , "daisy" , "dales" , "dally" , "dames" , "damns" , "damps" , "dance" , "dandy" , "dared" , "darer" , "dares" , "darks" , "darky" , "darns" , "darts" , "dashy" , "dated" , "dater" , "dates" , "datum" , "daubs" , "daunt" , "davit" , "dawns" , "dazed" , "dazes" , "deads" , "deals" , "dealt" , "deans" , "dears" , "deary" , "death" , "debar" , "debit" , "debts" , "debug" , "debut" , "decaf" , "decal" , "decay" , "decks" , "decor" , "decoy" , "decry" , "deeds" , "deems" , "deeps" , "defer" , "defog" , "defun" , "degas" , "degum" , "deice" , "deify" , "deign" , "deism" , "deist" , "deity" , "delay" , "delft" , "delis" , "dells" , "delta" , "delve" , "demit" , "demon" , "demos" , "demur" , "denim" , "dense" , "dents" , "depot" , "depth" , "deque" , "derby" , "desex" , "desks" , "deter" , "deuce" , "devil" , "dewed" , "dewey" , "dhows" , "dials" , "diary" , "diazo" , "diced" , "dicer" , "dices" , "dicey" , "dicks" , "dicky" , "dicot" , "dicta" , "dictu" , "dicut" , "diddy" , "didos" , "didot" , "didst" , "diems" , "diest" , "dieth" , "diets" , "digit" , "diked" , "dikes" , "dildo" , "dills" , "dilly" , "dimer" , "dimes" , "dimly" , "dinar" , "dined" , "diner" , "dines" , "dingo" , "dings" , "dingy" , "dinks" , "dinky" , "dints" , "diode" , "dippy" , "dipso" , "direr" , "dirge" , "dirks" , "dirts" , "dirty" , "disco" , "discs" , "dishy" , "disks" , "ditch" , "ditto" , "ditty" , "divan" , "divas" , "dived" , "diver" , "dives" , "divot" , "divvy" , "dixit" , "dizzy" , "djinn" , "docks" , "dodge" , "dodgy" , "dodos" , "doers" , "doest" , "doeth" , "doffs" , "doges" , "doggo" , "doggy" , "dogie" , "dogma" , "doily" , "doing" , "dolce" , "doled" , "doles" , "dolls" , "dolly" , "dolor" , "dolts" , "domed" , "domes" , "donee" , "donna" , "donor" , "donut" , "dooms" , "doors" , "doozy" , "doped" , "doper" , "dopes" , "dopey" , "dorks" , "dorky" , "dorms" , "dosed" , "doser" , "doses" , "doted" , "doter" , "dotes" , "dotty" , "doubt" , "dough" , "douse" , "doves" , "dovey" , "dowdy" , "dowel" , "dower" , "downs" , "downy" , "dowry" , "dowse" , "doxie" , "doyen" , "dozed" , "dozen" , "dozer" , "dozes" , "drabs" , "draft" , "drags" , "drain" , "drake" , "drama" , "drams" , "drank" , "drape" , "drawl" , "drawn" , "draws" , "drays" , "dread" , "dream" , "drear" , "dreck" , "dregs" , "dress" , "dribs" , "dried" , "drier" , "dries" , "drift" , "drill" , "drily" , "drink" , "drips" , "drive" , "droid" , "droll" , "drone" , "drool" , "droop" , "drops" , "dross" , "drove" , "drown" , "drubs" , "drugs" , "druid" , "drums" , "drunk" , "dryad" , "dryer" , "dryly" , "duals" , "ducal" , "ducat" , "duces" , "duchy" , "ducks" , "ducky" , "ducts" , "duddy" , "dudes" , "duels" , "duets" , "duffs" , "dukes" , "dulls" , "dully" , "dulse" , "dummy" , "dumps" , "dumpy" , "dunce" , "dunes" , "dungs" , "dungy" , "dunks" , "dunno" , "duomo" , "duped" , "duper" , "dupes" , "duple" , "durst" , "dusks" , "dusky" , "dusts" , "dusty" , "dutch" , "duvet" , "dwarf" , "dweeb" , "dwell" , "dwelt" , "dyads" , "dyers" , "dying" , "dykes" , "dynes" , "eager" , "eagle" , "eared" , "earls" , "early" , "earns" , "earth" , "eased" , "easel" , "eases" , "easts" , "eaten" , "eater" , "eaves" , "ebbed" , "ebony" , "echos" , "eclat" , "edema" , "edged" , "edger" , "edges" , "edict" , "edify" , "edits" , "educe" , "eerie" , "egads" , "egged" , "egger" , "egret" , "eider" , "eight" , "eject" , "eking" , "eland" , "elans" , "elate" , "elbow" , "elder" , "elect" , "elegy" , "elfin" , "elide" , "elite" , "elope" , "elude" , "elves" , "email" , "embed" , "ember" , "emcee" , "emend" , "emery" , "emirs" , "emits" , "emote" , "empty" , "enact" , "ended" , "ender" , "endow" , "endue" , "enema" , "enemy" , "enjoy" , "ennui" , "enrol" , "ensue" , "enter" , "entry" , "envoi" , "envoy" , "epact" , "epees" , "ephah" , "ephod" , "epics" , "epoch" , "epoxy" , "epsom" , "equal" , "equip" , "erase" , "erect" , "erode" , "erred" , "error" , "eruct" , "erupt" , "essay" , "esses" , "ester" , "estop" , "etext" , "ether" , "ethic" , "ethos" , "ethyl" , "etude" , "evade" , "evens" , "event" , "every" , "evict" , "evils" , "evoke" , "exact" , "exalt" , "exams" , "excel" , "excon" , "exeat" , "execs" , "exert" , "exile" , "exist" , "exits" , "expat" , "expel" , "expos" , "extol" , "extra" , "exude" , "exult" , "exurb" , "eyers" , "eying" , "eyrie" , "fable" , "faced" , "facer" , "faces" , "facet" , "facie" , "facto" , "facts" , "faddy" , "faded" , "fader" , "fades" , "faery" , "fagot" , "fails" , "faint" , "faire" , "fairs" , "fairy" , "faith" , "faked" , "faker" , "fakes" , "fakir" , "falls" , "false" , "famed" , "fames" , "fancy" , "fangs" , "fanin" , "fanny" , "farad" , "farce" , "fared" , "fares" , "farms" , "farts" , "fasts" , "fatal" , "fated" , "fates" , "fatly" , "fatso" , "fatty" , "fatwa" , "fault" , "fauna" , "fauns" , "favor" , "fawns" , "fawny" , "faxed" , "faxer" , "faxes" , "fazed" , "fazes" , "fears" , "feast" , "feats" , "fecal" , "feces" , "feeds" , "feels" , "feign" , "feint" , "feist" , "fella" , "fells" , "felon" , "felts" , "femme" , "femur" , "fence" , "fends" , "fenny" , "feral" , "fermi" , "ferns" , "ferny" , "ferry" , "fetal" , "fetch" , "feted" , "fetes" , "fetid" , "fetor" , "fetus" , "feuar" , "feuds" , "feued" , "fever" , "fewer" , "fiats" , "fiber" , "fibre" , "fiche" , "fichu" , "fiefs" , "field" , "fiend" , "fiery" , "fifes" , "fifth" , "fifty" , "fight" , "filar" , "filch" , "filed" , "filer" , "files" , "filet" , "fills" , "filly" , "films" , "filmy" , "filth" , "final" , "finch" , "finds" , "fined" , "finer" , "fines" , "finif" , "finis" , "finks" , "finny" , "fiord" , "fired" , "firer" , "fires" , "firma" , "firms" , "first" , "firth" , "fishy" , "fists" , "fisty" , "fitly" , "fiver" , "fives" , "fixed" , "fixer" , "fixes" , "fixit" , "fizzy" , "fjord" , "flabs" , "flack" , "flags" , "flail" , "flair" , "flake" , "flaks" , "flaky" , "flame" , "flams" , "flank" , "flaps" , "flare" , "flash" , "flask" , "flats" , "flaws" , "flays" , "fleas" , "fleck" , "flees" , "fleet" , "flesh" , "flick" , "flics" , "flied" , "flier" , "flies" , "fling" , "flint" , "flips" , "flirt" , "flits" , "float" , "flock" , "floes" , "flogs" , "flood" , "floor" , "flops" , "flora" , "floss" , "flour" , "flout" , "flown" , "flows" , "flubs" , "flues" , "fluff" , "fluid" , "fluke" , "fluky" , "flume" , "flung" , "flunk" , "flush" , "flute" , "flyby" , "flyer" , "foals" , "foams" , "foamy" , "focal" , "focus" , "fogey" , "foggy" , "foils" , "foist" , "folds" , "folia" , "folic" , "folio" , "folks" , "folky" , "folly" , "fondu" , "fonts" , "foods" , "fools" , "foots" , "foray" , "force" , "fords" , "fores" , "forge" , "forgo" , "forks" , "forky" , "forma" , "forms" , "forte" , "forth" , "forts" , "forty" , "forum" , "fossa" , "fosse" , "fouls" , "found" , "fount" , "fours" , "fovea" , "fowls" , "foxed" , "foxes" , "foyer" , "frail" , "frame" , "franc" , "frank" , "frats" , "fraud" , "frays" , "freak" , "freed" , "freer" , "frees" , "fresh" , "frets" , "friar" , "fried" , "frier" , "fries" , "frigs" , "frill" , "frisk" , "frizz" , "frock" , "frogs" , "frond" , "front" , "frosh" , "frost" , "froth" , "frown" , "froze" , "fruit" , "frump" , "fryer" , "ftped" , "fucks" , "fudge" , "fudgy" , "fuels" , "fugal" , "fugit" , "fugue" , "fulls" , "fully" , "fumed" , "fumer" , "fumes" , "funds" , "fungi" , "fungo" , "funks" , "funky" , "funny" , "furls" , "furor" , "furry" , "furze" , "fused" , "fusee" , "fuses" , "fussy" , "fusty" , "futon" , "fuzed" , "fuzes" , "fuzzy" , "gabby" , "gable" , "gaffe" , "gaffs" , "gages" , "gaily" , "gains" , "gaits" , "galas" , "gales" , "galls" , "gamba" , "gamed" , "gamer" , "games" , "gamey" , "gamic" , "gamin" , "gamma" , "gamut" , "ganef" , "gangs" , "gaols" , "gaped" , "gaper" , "gapes" , "gappy" , "garbs" , "garde" , "gases" , "gasps" , "gassy" , "gated" , "gates" , "gator" , "gaudy" , "gauge" , "gaunt" , "gauss" , "gauze" , "gauzy" , "gavel" , "gawks" , "gawky" , "gayer" , "gayly" , "gazed" , "gazer" , "gazes" , "gears" , "gecko" , "geeks" , "geese" , "gelds" , "genes" , "genet" , "genie" , "genii" , "genre" , "gents" , "genus" , "geode" , "geoid" , "germs" , "gesso" , "getup" , "ghost" , "ghoti" }
    austin_words |= { "ghoul" , "giant" , "gibed" , "giber" , "gibes" , "giddy" , "gifts" , "gigas" , "gigue" , "gilds" , "gills" , "gilts" , "gimel" , "gimme" , "gimps" , "gimpy" , "ginny" , "gipsy" , "girds" , "girls" , "girly" , "giros" , "girth" , "girts" , "gismo" , "gists" , "given" , "giver" , "gives" , "gizmo" , "glade" , "glads" , "gland" , "glans" , "glare" , "glary" , "glass" , "glaze" , "gleam" , "glean" , "glebe" , "glees" , "glens" , "glide" , "glint" , "glitz" , "gloat" , "globe" , "globs" , "gloms" , "gloom" , "glory" , "gloss" , "glove" , "glows" , "glued" , "gluer" , "glues" , "gluey" , "gluon" , "gluts" , "glyph" , "gnarl" , "gnash" , "gnats" , "gnaws" , "gnome" , "goads" , "goals" , "goats" , "godly" , "goers" , "goest" , "goeth" , "gofer" , "going" , "golds" , "golem" , "golfs" , "golly" , "gonad" , "goner" , "gongs" , "gonna" , "gonzo" , "goods" , "goody" , "gooey" , "goofs" , "goofy" , "gooks" , "gooky" , "goons" , "goony" , "goopy" , "goose" , "goosy" , "gored" , "gores" , "gorge" , "gorse" , "goths" , "gotta" , "gouda" , "gouge" , "gourd" , "gouts" , "gouty" , "gowns" , "goyim" , "grabs" , "grace" , "grade" , "grads" , "graft" , "grail" , "grain" , "grams" , "grand" , "grant" , "grape" , "graph" , "grapy" , "grasp" , "grass" , "grata" , "grate" , "grave" , "gravy" , "grays" , "graze" , "great" , "grebe" , "greed" , "greek" , "green" , "greet" , "greps" , "greys" , "grids" , "grief" , "grift" , "grill" , "grime" , "grimy" , "grind" , "grins" , "gripe" , "grips" , "grist" , "grits" , "groan" , "groat" , "grody" , "grogs" , "groin" , "groks" , "gronk" , "grook" , "groom" , "grope" , "gross" , "group" , "grout" , "grove" , "growl" , "grown" , "grows" , "grubs" , "gruel" , "gruff" , "grump" , "grunt" , "guano" , "guard" , "guava" , "guess" , "guest" , "guide" , "guild" , "guile" , "guilt" , "guise" , "gulag" , "gulch" , "gules" , "gulfs" , "gulls" , "gully" , "gulps" , "gumbo" , "gummy" , "gunks" , "gunky" , "gunny" , "guppy" , "gurus" , "gushy" , "gusto" , "gusts" , "gusty" , "gutsy" , "gutta" , "gutty" , "guyed" , "gwine" , "gyppy" , "gypsy" , "gyros" , "gyved" , "gyves" , "habit" , "hacks" , "hadda" , "hades" , "hadst" , "hafta" , "hafts" , "haiku" , "hails" , "hairs" , "hairy" , "haled" , "haler" , "hales" , "hallo" , "halls" , "halma" , "halos" , "halts" , "halve" , "hames" , "hammy" , "hamza" , "hands" , "handy" , "hangs" , "hanks" , "hanky" , "hapax" , "haply" , "happy" , "hardy" , "harem" , "hares" , "harks" , "harms" , "harps" , "harpy" , "harry" , "harsh" , "harts" , "harum" , "hasps" , "haste" , "hasty" , "hatch" , "hated" , "hater" , "hates" , "hauls" , "haunt" , "haute" , "haven" , "haves" , "havoc" , "hawed" , "hawks" , "hayed" , "hayer" , "hayey" , "hazed" , "hazel" , "hazer" , "hazes" , "heads" , "heady" , "heals" , "heaps" , "heard" , "hears" , "heart" , "heath" , "heats" , "heave" , "heavy" , "hedge" , "heeds" , "heels" , "heerd" , "hefts" , "hefty" , "heigh" , "heirs" , "heist" , "helix" , "hello" , "hells" , "helms" , "helps" , "hemps" , "hempy" , "hence" , "henge" , "henna" , "henry" , "herbs" , "herby" , "herds" , "herem" , "heres" , "heron" , "heros" , "hertz" , "hewed" , "hewer" , "hexad" , "hexed" , "hexer" , "hexes" , "hicks" , "hider" , "hides" , "highs" , "hiked" , "hiker" , "hikes" , "hilar" , "hills" , "hilly" , "hilts" , "hilum" , "himbo" , "hinds" , "hinge" , "hints" , "hippo" , "hippy" , "hired" , "hirer" , "hires" , "hitch" , "hived" , "hiver" , "hives" , "hoagy" , "hoard" , "hoars" , "hoary" , "hobby" , "hobos" , "hocks" , "hocus" , "hodad" , "hoers" , "hogan" , "hoist" , "hokey" , "hokum" , "holds" , "holed" , "holer" , "holes" , "holey" , "holly" , "holon" , "homed" , "homer" , "homes" , "homey" , "homme" , "homos" , "honed" , "honer" , "hones" , "honey" , "honks" , "honky" , "honor" , "hooch" , "hoods" , "hooey" , "hoofs" , "hooks" , "hooky" , "hoops" , "hoots" , "hoped" , "hoper" , "hopes" , "hoppy" , "horde" , "horns" , "horny" , "horse" , "horsy" , "hosed" , "hoses" , "hosts" , "hotel" , "hotly" , "hound" , "houri" , "hours" , "house" , "hovel" , "hover" , "howdy" , "howls" , "hubba" , "hubby" , "huffs" , "huffy" , "huger" , "hulas" , "hulks" , "hulky" , "hullo" , "hulls" , "human" , "humid" , "humor" , "humpf" , "humph" , "humps" , "humpy" , "humus" , "hunch" , "hunks" , "hunky" , "hunts" , "hurls" , "hurly" , "hurry" , "hurts" , "husks" , "husky" , "hussy" , "hutch" , "huzza" , "hydra" , "hydro" , "hyena" , "hying" , "hymen" , "hymns" , "hyped" , "hyper" , "hypes" , "hypos" , "iambs" , "icers" , "ichor" , "icier" , "icily" , "icing" , "icons" , "ideal" , "ideas" , "idiom" , "idiot" , "idled" , "idler" , "idles" , "idols" , "idyll" , "idyls" , "igloo" , "ikats" , "ikons" , "ileum" , "ileus" , "iliac" , "ilium" , "image" , "imago" , "imams" , "imbed" , "imbue" , "immix" , "impel" , "imply" , "impro" , "inane" , "inapt" , "incur" , "index" , "indie" , "inept" , "inert" , "infer" , "infix" , "infra" , "ingot" , "injun" , "inked" , "inker" , "inlay" , "inlet" , "inner" , "inode" , "input" , "inset" , "inter" , "intra" , "intro" , "inure" , "ioctl" , "iodic" , "ionic" , "iotas" , "irate" , "irked" , "irons" , "irony" , "isles" , "islet" , "issue" , "itchy" , "items" , "ivied" , "ivies" , "ivory" , "ixnay" , "jacks" , "jaded" , "jades" , "jaggy" , "jails" , "jakes" , "jambs" , "jammy" , "janes" , "japan" , "jaunt" , "jawed" , "jazzy" , "jeans" , "jeeps" , "jeers" , "jello" , "jells" , "jelly" , "jenny" , "jerks" , "jerky" , "jerry" , "jests" , "jetty" , "jewel" , "jibed" , "jiber" , "jibes" , "jiffs" , "jiffy" , "jihad" , "jilts" , "jimmy" , "jingo" , "jings" , "jinks" , "jinns" , "jived" , "jives" , "jocks" , "joeys" , "johns" , "joins" , "joint" , "joist" , "joked" , "joker" , "jokes" , "jolly" , "jolts" , "joule" , "joust" , "jowls" , "jowly" , "joyed" , "judge" , "judos" , "juice" , "juicy" , "jujus" , "jukes" , "julep" , "jumbo" , "jumps" , "jumpy" , "junco" , "junks" , "junky" , "junta" , "juror" , "juste" , "jutes" , "kabob" , "kaiak" , "kales" , "kapok" , "kappa" , "kaput" , "karat" , "karma" , "kayak" , "kayos" , "kazoo" , "kebab" , "kebob" , "keels" , "keens" , "keeps" , "kefir" , "kelly" , "kelps" , "kelpy" , "kenaf" , "kepis" , "kerbs" , "kerfs" , "kerns" , "ketch" , "keyed" , "keyer" , "khaki" , "khans" , "kicks" , "kicky" , "kiddo" , "kikes" , "kills" , "kilns" , "kilos" , "kilts" , "kilty" , "kinda" , "kinds" , "kings" , "kinks" , "kinky" , "kiosk" , "kirks" , "kited" , "kites" , "kiths" , "kitty" , "kivas" , "kiwis" , "klieg" , "kluge" , "klugy" , "klunk" , "klutz" , "knack" , "knave" , "knead" , "kneed" , "kneel" , "knees" , "knell" , "knelt" , "knife" , "knish" , "knits" , "knobs" , "knock" , "knoll" , "knops" , "knots" , "knout" , "known" , "knows" , "knurl" , "koala" , "koine" , "kooks" , "kooky" , "kopek" , "kraal" , "kraut" , "krill" , "krona" , "krone" , "kudos" , "kudzu" , "kulak" , "kyrie" , "label" , "labia" , "labor" , "laced" , "lacer" , "laces" , "lacey" , "lacks" , "laded" , "laden" , "lades" , "ladle" , "lager" , "laird" , "lairs" , "laity" , "laker" , "lakes" , "lamas" , "lambs" , "lamed" , "lamer" , "lames" , "lamps" , "lanai" , "lance" , "lands" , "lanes" , "lanky" , "lapel" , "lapin" , "lapis" , "lapse" , "larch" , "lards" , "lardy" , "large" , "largo" , "larks" , "larva" , "lased" , "laser" , "lases" , "lasso" , "lasts" , "latch" , "later" , "latex" , "lathe" , "laths" , "latin" , "latus" , "laude" , "lauds" , "laugh" , "lavas" , "laved" , "laver" , "laves" , "lawns" , "lawny" , "lawzy" , "laxer" , "laxly" , "layer" , "layup" , "lazed" , "lazes" , "leach" , "leads" , "leafs" , "leafy" , "leaks" , "leaky" , "leans" , "leant" , "leaps" , "leapt" , "learn" , "lease" , "leash" , "least" , "leave" , "ledge" , "leech" , "leeks" , "leers" , "leery" , "lefts" , "lefty" , "legal" , "leggo" , "leggy" , "legit" , "legos" , "lemma" , "lemme" , "lemon" , "lemur" , "lends" , "lento" , "leper" , "lepta" , "letup" , "levee" , "level" , "lever" , "levis" , "liars" , "libel" , "libra" , "licit" , "licks" , "liege" , "liens" , "liers" , "liest" , "lieth" , "lifer" , "lifts" , "light" , "ligne" , "liked" , "liken" , "liker" , "likes" , "lilac" , "lilts" , "lilty" , "limbo" , "limbs" , "limby" , "limed" , "limen" , "limes" , "limey" , "limit" , "limns" , "limos" , "limps" , "lined" , "linen" , "liner" , "lines" , "lingo" , "lings" , "links" , "lints" , "linty" , "lions" , "lipid" , "lippy" , "liras" , "lisle" , "lisps" , "lists" , "liter" , "lites" , "lithe" , "litho" , "litre" , "lived" , "liven" , "liver" , "lives" , "livid" , "livre" , "llama" , "loads" , "loafs" , "loams" , "loamy" , "loans" , "loath" , "lobar" , "lobby" , "lobed" , "lobes" , "local" , "lochs" , "locks" , "locos" , "locus" , "lodes" , "lodge" , "loess" , "lofts" , "lofty" , "loges" , "loggy" , "logic" , "login" , "logos" , "loins" , "lolls" , "lolly" , "loner" , "longs" , "looks" , "looky" , "looms" , "loons" , "loony" , "loops" , "loopy" , "loose" , "loots" , "loped" , "loper" , "lopes" , "loppy" , "lords" , "lordy" , "lores" , "lorry" , "loser" , "loses" , "lossy" , "lotsa" , "lotta" , "lotto" , "lotus" , "louis" , "louse" , "lousy" , "louts" , "loved" , "lover" , "loves" , "lowed" , "lower" , "lowly" , "loxes" , "loyal" , "luaus" , "lubes" , "lubra" , "lucid" , "lucks" , "lucky" , "lucre" , "lulab" , "lulls" , "lulus" , "lumen" , "lumps" , "lumpy" , "lunar" , "lunch" , "lunes" , "lunge" , "lungs" , "lupus" , "lurch" , "lured" , "lurer" , "lures" , "lurid" , "lurks" , "lusts" , "lusty" , "luted" , "lutes" , "luvya" , "luxes" , "lycra" , "lying" , "lymph" , "lynch" , "lyres" , "lyric" , "macaw" , "maced" , "macer" , "maces" , "macho" , "macro" , "madam" , "madly" , "mafia" , "magic" , "magma" , "magna" , "magus" , "mahua" , "maids" , "mails" , "maims" , "mains" , "maize" , "major" , "maker" , "makes" , "males" , "malls" , "malts" , "malty" , "mamas" , "mambo" , "mamma" , "mammy" , "maned" , "manes" , "mange" , "mango" , "mangy" , "mania" , "manic" , "manly" } 
    austin_words |= { "manna" , "manor" , "manse" , "manta" , "maple" , "march" , "mares" , "marge" , "maria" , "marks" , "marls" , "marry" , "marsh" , "marts" , "maser" , "mashy" , "masks" , "mason" , "masse" , "masts" , "match" , "mated" , "mater" , "mates" , "matey" , "maths" , "matte" , "matzo" , "mauls" , "mauve" , "maven" , "mavis" , "maxim" , "maxis" , "maybe" , "mayor" , "mayst" , "mazed" , "mazer" , "mazes" , "meads" , "meals" , "mealy" , "means" , "meant" , "meany" , "meats" , "meaty" , "mebbe" , "mecca" , "mecum" , "medal" , "media" , "medic" , "meets" , "melba" , "melds" , "melee" , "melon" , "melts" , "memes" , "memos" , "mends" , "menus" , "meows" , "mercy" , "merge" , "merit" , "merry" , "merse" , "mesas" , "mesne" , "meson" , "messy" , "metal" , "meted" , "meter" , "metes" , "metre" , "metro" , "mewed" , "mezzo" , "miaow" , "micas" , "micks" , "micro" , "middy" , "midis" , "midst" , "miens" , "miffs" , "might" , "miked" , "mikes" , "milch" , "miler" , "miles" , "milks" , "milky" , "mills" , "mimed" , "mimeo" , "mimer" , "mimes" , "mimic" , "mimsy" , "minas" , "mince" , "minds" , "mined" , "miner" , "mines" , "minim" , "minis" , "minks" , "minor" , "mints" , "minus" , "mired" , "mires" , "mirth" , "miser" , "missy" , "mists" , "misty" , "miter" , "mites" , "mitre" , "mitts" , "mixed" , "mixer" , "mixes" , "mixup" , "moans" , "moats" , "mocha" , "mocks" , "modal" , "model" , "modem" , "modes" , "modus" , "mogul" , "mohel" , "moire" , "moist" , "molal" , "molar" , "molas" , "molds" , "moldy" , "moles" , "molls" , "molly" , "molto" , "molts" , "momma" , "mommy" , "monad" , "mondo" , "money" , "monic" , "monks" , "monte" , "month" , "mooch" , "moods" , "moody" , "mooed" , "moola" , "moons" , "moony" , "moors" , "moose" , "moots" , "moped" , "moper" , "mopes" , "moral" , "moray" , "morel" , "mores" , "morns" , "moron" , "morph" , "morts" , "mosey" , "mossy" , "mosts" , "motel" , "motes" , "motet" , "moths" , "mothy" , "motif" , "motor" , "motto" , "mould" , "moult" , "mound" , "mount" , "mourn" , "mouse" , "mousy" , "mouth" , "moved" , "mover" , "moves" , "movie" , "mowed" , "mower" , "moxie" , "mrads" , "mucho" , "mucks" , "mucky" , "mucus" , "muddy" , "muffs" , "mufti" , "muggy" , "mujik" , "mulch" , "mulct" , "mules" , "muley" , "mulls" , "mumbo" , "mummy" , "mumps" , "munch" , "munge" , "mungs" , "mungy" , "muons" , "mural" , "murks" , "murky" , "mused" , "muser" , "muses" , "mushy" , "music" , "musks" , "musky" , "musos" , "mussy" , "musta" , "musts" , "musty" , "muted" , "muter" , "mutes" , "mutts" , "muxes" , "mylar" , "mynah" , "mynas" , "myrrh" , "myths" , "nabla" , "nabob" , "nacho" , "nadir" , "naiad" , "nails" , "naive" , "naked" , "named" , "namer" , "names" , "nanny" , "napes" , "nappy" , "narco" , "narcs" , "nards" , "nares" , "nasal" , "nasty" , "natal" , "natch" , "nates" , "natty" , "naval" , "navel" , "naves" , "nears" , "neath" , "neato" , "necks" , "needs" , "needy" , "negro" , "neigh" , "neons" , "nerds" , "nerdy" , "nerfs" , "nerts" , "nerve" , "nervy" , "nests" , "never" , "newel" , "newer" , "newly" , "newsy" , "newts" , "nexus" , "nicad" , "nicer" , "niche" , "nicks" , "niece" , "nifty" , "night" , "nihil" , "nimbi" , "nines" , "ninja" , "ninny" , "ninth" , "nippy" , "nisei" , "niter" , "nitro" , "nitty" , "nixed" , "nixes" , "nixie" , "nobby" , "noble" , "nobly" , "nodal" , "noddy" , "nodes" , "noels" , "nohow" , "noire" , "noise" , "noisy" , "nomad" , "nonce" , "nones" , "nonny" , "nooks" , "nooky" , "noons" , "noose" , "norms" , "north" , "nosed" , "noses" , "nosey" , "notch" , "noted" , "noter" , "notes" , "nouns" , "novae" , "novas" , "novel" , "noway" , "nuder" , "nudes" , "nudge" , "nudie" , "nuked" , "nukes" , "nulls" , "numbs" , "nurbs" , "nurse" , "nutsy" , "nutty" , "nylon" , "nymph" , "oaken" , "oakum" , "oared" , "oases" , "oasis" , "oaten" , "oaths" , "obeah" , "obese" , "obeys" , "obits" , "oboes" , "occur" , "ocean" , "ocher" , "ochre" , "octal" , "octet" , "odder" , "oddly" , "odium" , "odors" , "odour" , "offal" , "offed" , "offen" , "offer" , "often" , "ogled" , "ogler" , "ogles" , "ogres" , "ohhhh" , "ohmic" , "oiled" , "oiler" , "oinks" , "oinky" , "okapi" , "okays" , "okras" , "olden" , "older" , "oldie" , "oleos" , "olios" , "olive" , "ombre" , "omega" , "omens" , "omits" , "oncet" , "onion" , "onset" , "oodle" , "oomph" , "oozed" , "oozes" , "opals" , "opens" , "opera" , "opine" , "opium" , "opted" , "optic" , "orals" , "orate" , "orbed" , "orbit" , "orcas" , "order" , "organ" , "oring" , "orlon" , "ortho" , "osier" , "other" , "otter" , "ought" , "ouija" , "ounce" , "ousel" , "ousts" , "outdo" , "outen" , "outer" , "outgo" , "outta" , "ouzel" , "ovals" , "ovary" , "ovate" , "ovens" , "overs" , "overt" , "ovoid" , "ovule" , "owest" , "oweth" , "owing" , "owlet" , "owned" , "owner" , "oxbow" , "oxeye" , "oxide" , "oxlip" , "ozone" , "paced" , "pacer" , "paces" , "packs" , "pacts" , "paddy" , "padre" , "paean" , "pagan" , "paged" , "pager" , "pages" , "pails" , "pains" , "paint" , "pairs" , "paled" , "paler" , "pales" , "palls" , "pally" , "palms" , "palmy" , "palsy" , "pampa" , "panda" , "paned" , "panel" , "panes" , "panga" , "pangs" , "panic" , "pansy" , "pants" , "panty" , "papal" , "papas" , "papaw" , "paper" , "pappy" , "paras" , "parch" , "pards" , "pared" , "paren" , "parer" , "pares" , "parka" , "parks" , "parry" , "parse" , "parts" , "party" , "pasha" , "passe" , "pasta" , "paste" , "pasts" , "pasty" , "patch" , "paten" , "pater" , "pates" , "paths" , "patio" , "patsy" , "patty" , "pause" , "pavan" , "paved" , "paver" , "paves" , "pawed" , "pawer" , "pawky" , "pawls" , "pawns" , "payed" , "payee" , "payer" , "peace" , "peach" , "peaks" , "peaky" , "peals" , "pearl" , "pears" , "pease" , "peats" , "peaty" , "pecan" , "pecks" , "pedal" , "peeks" , "peels" , "peens" , "peeps" , "peers" , "peeve" , "pekoe" , "pelts" , "penal" , "pence" , "pends" , "penes" , "pengo" , "penis" , "penny" , "peons" , "peony" , "peppy" , "perch" , "perdu" , "peril" , "perks" , "perky" , "perms" , "pesky" , "pesos" , "pesto" , "pests" , "petal" , "peter" , "petit" , "petri" , "petty" , "pewee" , "pewit" , "pffft" , "phage" , "phase" , "phial" , "phlox" , "phone" , "phony" , "photo" , "phyla" , "piano" , "picas" , "picks" , "picky" , "picot" , "piece" , "piers" , "pieta" , "piety" , "piggy" , "pigmy" , "piing" , "piker" , "pikes" , "pilaf" , "pilau" , "piled" , "piles" , "pills" , "pilot" , "pimps" , "pinch" , "pined" , "pines" , "piney" , "pings" , "pinko" , "pinks" , "pinky" , "pinto" , "pints" , "pinup" , "pions" , "pious" , "piped" , "piper" , "pipes" , "pipet" , "pique" , "pismo" , "pitas" , "pitch" , "piths" , "pithy" , "piton" , "pivot" , "pixel" , "pixie" , "pizza" , "place" , "plaid" , "plain" , "plait" , "plane" , "plank" , "plans" , "plant" , "plash" , "plasm" , "plate" , "plats" , "playa" , "plays" , "plaza" , "plead" , "pleas" , "pleat" , "plebe" , "plebs" , "plein" , "plena" , "plied" , "plies" , "plink" , "plods" , "plonk" , "plops" , "plots" , "plows" , "ploys" , "pluck" , "plugs" , "plumb" , "plume" , "plump" , "plums" , "plumy" , "plunk" , "plush" , "plyer" , "poach" , "pocks" , "pocky" , "podgy" , "podia" , "poems" , "poesy" , "poets" , "point" , "poise" , "poked" , "poker" , "pokes" , "pokey" , "polar" , "poled" , "poler" , "poles" , "polio" , "polis" , "polka" , "polls" , "polly" , "polos" , "polyp" , "pomps" , "ponds" , "pones" , "pooch" , "pooey" , "poohs" , "pools" , "poops" , "popes" , "poppy" , "porch" , "pored" , "pores" , "porgy" , "porks" , "porky" , "porno" , "ports" , "posed" , "poser" , "poses" , "poset" , "posit" , "posse" , "poste" , "posts" , "potty" , "pouch" , "poufs" , "pound" , "pours" , "pouts" , "power" , "poxed" , "poxes" , "prams" , "prank" , "prate" , "prats" , "prawn" , "prays" , "preen" , "preps" , "press" , "prest" , "prexy" , "preys" , "price" , "prick" , "pride" , "pried" , "prier" , "pries" , "prigs" , "prima" , "prime" , "primo" , "primp" , "prims" , "prink" , "print" , "prior" , "prise" , "prism" , "privy" , "prize" , "probe" , "prods" , "proem" , "profs" , "promo" , "proms" , "prone" , "prong" , "proof" , "props" , "prose" , "prosy" , "proud" , "prove" , "prowl" , "prows" , "proxy" , "prude" , "prune" , "pruta" , "pryer" , "psalm" , "pseud" , "pshaw" , "psoas" , "pssst" , "psych" , "pubes" , "pubic" , "pubis" , "pucks" , "pudgy" , "puffs" , "puffy" , "puked" , "pukes" , "pukka" , "pulls" , "pulps" , "pulpy" , "pulse" , "pumas" , "pumps" , "punch" , "punks" , "punky" , "punny" , "punts" , "pupae" , "pupal" , "pupas" , "pupil" , "puppy" , "puree" , "purer" , "purge" , "purls" , "purrs" , "purse" , "purty" , "pushy" , "pussy" , "putts" , "putty" , "pygmy" , "pylon" , "pyres" , "pyxie" , "qophs" , "quack" , "quads" , "quaff" , "quail" , "quais" , "quake" , "qualm" , "quals" , "quark" , "quart" , "quash" , "quasi" , "quays" , "queen" , "queer" , "quell" , "query" , "quest" , "queue" , "quick" , "quids" , "quiet" , "quiff" , "quill" , "quilt" , "quint" , "quips" , "quipu" , "quire" , "quirk" , "quirt" , "quite" , "quits" , "quoin" , "quoit" , "quota" , "quote" , "quoth" , "rabbi" , "rabid" , "raced" , "racer" , "races" , "racks" , "radar" , "radii" , "radio" , "radix" , "radon" , "rafts" , "raged" , "rages" , "raids" , "rails" , "rains" , "rainy" , "raise" , "rajah" , "rajas" , "raked" , "raker" , "rakes" , "rally" , "ramps" , "ranch" , "rands" , "randy" , "range" , "rangy" , "ranks" , "rants" , "raped" , "raper" , "rapes" , "rapid" , "rarer" , "rasae" , "rasps" , "raspy" , "rated" , "rater" , "rates" , "raths" , "ratio" , "ratty" , "raved" , "ravel" , "raven" , "raver" , "raves" , "rawer" , "rawly" , "rayed" , "rayon" , "razed" , "razer" , "razes" , "razor" , "reach" , "react" , "reads" , "ready" , "realm" , "reals" , "reams" , "reaps" , "rearm" , "rears" , "rebar" , "rebel" , "rebid" , "rebox" , "rebus" , "rebut" , "recap" , "recta" , "recto" , "recur" , "recut" , "redid" , "redip" , "redly" , "redox" , "redux" }
    austin_words |= { "reeds" , "reedy" , "reefs" , "reeks" , "reeky" , "reels" , "reeve" , "refer" , "refit" , "refix" , "refly" , "refry" , "regal" , "rehab" , "reify" , "reign" , "reins" , "relax" , "relay" , "relet" , "relic" , "reman" , "remap" , "remit" , "remix" , "renal" , "rends" , "renew" , "rente" , "rents" , "repay" , "repel" , "reply" , "repro" , "reran" , "rerun" , "resaw" , "resay" , "reset" , "resew" , "resin" , "rests" , "retch" , "retro" , "retry" , "reuse" , "revel" , "revet" , "revue" , "rewed" , "rheas" , "rheum" , "rhino" , "rhumb" , "rhyme" , "rials" , "ribby" , "riced" , "ricer" , "rices" , "rider" , "rides" , "ridge" , "ridgy" , "rifer" , "rifle" , "rifts" , "right" , "rigid" , "rigor" , "riled" , "riles" , "rille" , "rills" , "rimed" , "rimer" , "rimes" , "rinds" , "rings" , "rinks" , "rinse" , "riots" , "ripen" , "riper" , "risen" , "riser" , "rises" , "risks" , "risky" , "rites" , "ritzy" , "rival" , "rived" , "riven" , "river" , "rives" , "rivet" , "roach" , "roads" , "roams" , "roans" , "roars" , "roast" , "robed" , "robes" , "robin" , "roble" , "robot" , "rocks" , "rocky" , "rodeo" , "roger" , "rogue" , "roids" , "roils" , "roily" , "roles" , "rolls" , "roman" , "romps" , "rondo" , "roods" , "roofs" , "rooks" , "rooky" , "rooms" , "roomy" , "roost" , "roots" , "rooty" , "roped" , "roper" , "ropes" , "roses" , "rosin" , "rotor" , "rouge" , "rough" , "round" , "rouse" , "roust" , "route" , "routs" , "roved" , "rover" , "roves" , "rowan" , "rowdy" , "rowed" , "rower" , "royal" , "rubes" , "ruble" , "ruche" , "ruddy" , "ruder" , "ruffs" , "rugby" , "ruing" , "ruins" , "ruled" , "ruler" , "rules" , "rumba" , "rumen" , "rummy" , "rumor" , "rumps" , "runes" , "rungs" , "runic" , "runny" , "runts" , "runty" , "rupee" , "rural" , "ruses" , "rusks" , "russe" , "rusts" , "rusty" , "rutty" , "saber" , "sable" , "sabra" , "sabre" , "sacks" , "sadly" , "safer" , "safes" , "sagas" , "sager" , "sages" , "sahib" , "sails" , "saint" , "saith" , "sakes" , "salad" , "sales" , "sally" , "salon" , "salsa" , "salts" , "salty" , "salve" , "salvo" , "samba" , "sands" , "sandy" , "saner" , "sappy" , "saran" , "sarge" , "saris" , "sassy" , "sated" , "sates" , "satin" , "satyr" , "sauce" , "saucy" , "sauna" , "saute" , "saved" , "saver" , "saves" , "savor" , "savvy" , "sawed" , "sawer" , "saxes" , "sayer" , "scabs" , "scads" , "scald" , "scale" , "scalp" , "scaly" , "scamp" , "scams" , "scans" , "scant" , "scare" , "scarf" , "scarp" , "scars" , "scary" , "scats" , "scene" , "scent" , "schmo" , "schwa" , "scion" , "scoff" , "scold" , "scone" , "scoop" , "scoot" , "scope" , "scops" , "score" , "scorn" , "scour" , "scout" , "scowl" , "scows" , "scram" , "scrap" , "screw" , "scrim" , "scrip" , "scrod" , "scrub" , "scrum" , "scuba" , "scudi" , "scudo" , "scuds" , "scuff" , "scull" , "scums" , "scurf" , "scuse" , "scuzz" , "seals" , "seams" , "seamy" , "sears" , "seats" , "sebum" , "secco" , "sects" , "sedan" , "seder" , "sedge" , "sedgy" , "sedum" , "seeds" , "seedy" , "seeks" , "seems" , "seeps" , "seers" , "seest" , "seeth" , "segue" , "seine" , "seize" , "selah" , "selfs" , "sells" , "semen" , "semis" , "sends" , "sense" , "sepal" , "sepia" , "sepoy" , "septa" , "serfs" , "serge" , "serif" , "serum" , "serve" , "servo" , "setup" , "seven" , "sever" , "sewed" , "sewer" , "sexed" , "sexes" , "shack" , "shade" , "shads" , "shady" , "shaft" , "shags" , "shahs" , "shake" , "shako" , "shaky" , "shale" , "shall" , "shalt" , "shame" , "shams" , "shank" , "shape" , "shard" , "share" , "shark" , "sharp" , "shave" , "shawl" , "shawm" , "shays" , "sheaf" , "shear" , "sheds" , "sheen" , "sheep" , "sheer" , "sheet" , "sheik" , "shelf" , "shell" , "sherd" , "shews" , "shied" , "shier" , "shies" , "shift" , "shiki" , "shill" , "shims" , "shine" , "shins" , "shiny" , "ships" , "shire" , "shirk" , "shirr" , "shirt" , "shish" , "shits" , "shlep" , "shmoo" , "shnor" , "shoal" , "shoat" , "shock" , "shoed" , "shoer" , "shoes" , "shoji" , "shone" , "shook" , "shoos" , "shoot" , "shops" , "shore" , "shorn" , "short" , "shots" , "shout" , "shove" , "shown" , "shows" , "showy" , "shred" , "shrew" , "shrub" , "shrug" , "shuck" , "shuns" , "shunt" , "shush" , "shute" , "shuts" , "shyer" , "shyly" , "sibyl" , "sicko" , "sicks" , "sided" , "sides" , "sidle" , "siege" , "sieve" , "sifts" , "sighs" , "sight" , "sigma" , "signs" , "silks" , "silky" , "sills" , "silly" , "silos" , "silts" , "silty" , "since" , "sines" , "sinew" , "singe" , "sings" , "sinks" , "sinus" , "sired" , "siree" , "siren" , "sires" , "sirup" , "sisal" , "sissy" , "sitar" , "sited" , "sites" , "situs" , "sixes" , "sixth" , "sixty" , "sized" , "sizer" , "sizes" , "skate" , "skeet" , "skein" , "skews" , "skids" , "skied" , "skier" , "skies" , "skiff" , "skill" , "skimp" , "skims" , "skins" , "skint" , "skips" , "skirt" , "skits" , "skoal" , "skulk" , "skull" , "skunk" , "skyed" , "slabs" , "slack" , "slags" , "slain" , "slake" , "slams" , "slang" , "slant" , "slaps" , "slash" , "slate" , "slats" , "slave" , "slaws" , "slays" , "sleds" , "sleek" , "sleep" , "sleet" , "slept" , "slews" , "slice" , "slick" , "slide" , "slier" , "slily" , "slime" , "slims" , "slimy" , "sling" , "slink" , "slips" , "slits" , "slobs" , "sloes" , "slogs" , "slomo" , "sloop" , "slope" , "slops" , "slosh" , "sloth" , "slots" , "slows" , "slued" , "slues" , "sluff" , "slugs" , "slump" , "slums" , "slung" , "slunk" , "slurp" , "slurs" , "slush" , "sluts" , "slyer" , "slyly" , "smack" , "small" , "smart" , "smash" , "smear" , "smell" , "smelt" , "smile" , "smirk" , "smite" , "smith" , "smock" , "smogs" , "smoke" , "smoky" , "smote" , "smurf" , "smuts" , "snack" , "snafu" , "snags" , "snail" , "snake" , "snaky" , "snaps" , "snare" , "snarf" , "snark" , "snarl" , "sneak" , "sneer" , "snide" , "sniff" , "snipe" , "snips" , "snits" , "snobs" , "snood" , "snook" , "snoop" , "snoot" , "snore" , "snort" , "snots" , "snout" , "snows" , "snowy" , "snubs" , "snuck" , "snuff" , "snugs" , "soaks" , "soaps" , "soapy" , "soars" , "sober" , "socko" , "socks" , "socle" , "sodas" , "sofas" , "softs" , "softy" , "soggy" , "soils" , "solar" , "soled" , "soles" , "solid" , "solon" , "solos" , "solum" , "solve" , "somas" , "sonar" , "songs" , "sonic" , "sonly" , "sonny" , "sooth" , "soots" , "sooty" , "soppy" , "sorer" , "sores" , "sorry" , "sorta" , "sorts" , "souls" , "sound" , "soups" , "soupy" , "sours" , "souse" , "south" , "sowed" , "sower" , "soyas" , "space" , "spacy" , "spade" , "spake" , "spang" , "spank" , "spans" , "spare" , "spark" , "spars" , "spasm" , "spate" , "spats" , "spawn" , "spays" , "spazz" , "speak" , "spear" , "speck" , "specs" , "speed" , "spell" , "spelt" , "spend" , "spent" , "sperm" , "spews" , "spice" , "spics" , "spicy" , "spied" , "spiel" , "spier" , "spies" , "spiff" , "spike" , "spiky" , "spill" , "spilt" , "spina" , "spine" , "spins" , "spiny" , "spire" , "spite" , "spits" , "spitz" , "spivs" , "splat" , "splay" , "split" , "spoil" , "spoke" , "spoof" , "spook" , "spool" , "spoon" , "spoor" , "spore" , "sport" , "spots" , "spout" , "sprat" , "spray" , "spree" , "sprig" , "sprit" , "sprog" , "sprue" , "spuds" , "spued" , "spume" , "spumy" , "spunk" , "spurn" , "spurs" , "spurt" , "sputa" , "squab" , "squad" , "squat" , "squaw" , "squib" , "squid" , "stabs" , "stack" , "staff" , "stage" , "stags" , "stagy" , "staid" , "stain" , "stair" , "stake" , "stale" , "stalk" , "stall" , "stamp" , "stand" , "stank" , "staph" , "stare" , "stark" , "stars" , "start" , "stash" , "state" , "stats" , "stave" , "stays" , "stead" , "steak" , "steal" , "steam" , "steed" , "steel" , "steep" , "steer" , "stein" , "stela" , "stele" , "stems" , "steno" , "steps" , "stern" , "stets" , "stews" , "stick" , "stied" , "sties" , "stiff" , "stile" , "still" , "stilt" , "sting" , "stink" , "stint" , "stirs" , "stoae" , "stoas" , "stoat" , "stock" , "stogy" , "stoic" , "stoke" , "stole" , "stoma" , "stomp" , "stone" , "stony" , "stood" , "stool" , "stoop" , "stops" , "store" , "stork" , "storm" , "story" , "stoup" , "stout" , "stove" , "stows" , "strap" , "straw" , "stray" , "strep" , "strew" , "strip" , "strop" , "strum" , "strut" , "stubs" , "stuck" , "studs" , "study" , "stuff" , "stump" , "stung" , "stunk" , "stuns" , "stunt" , "styes" , "style" , "styli" , "suave" , "sucks" , "sudsy" , "suede" , "suers" , "suets" , "suety" , "sugar" , "suing" , "suite" , "suits" , "sulfa" , "sulks" , "sulky" , "sully" , "sumac" , "summa" , "sumps" , "sunny" , "sunup" , "super" , "supes" , "supra" , "suras" , "surds" , "surer" , "surfs" , "surge" , "surly" , "sushi" , "sutra" , "swabs" , "swags" , "swain" , "swami" , "swamp" , "swank" , "swans" , "swaps" , "sward" , "sware" , "swarf" , "swarm" , "swart" , "swash" , "swath" , "swats" , "sways" , "swear" , "sweat" , "swede" , "sweep" , "sweet" , "swell" , "swept" , "swift" , "swigs" , "swill" , "swims" , "swine" , "swing" , "swipe" , "swirl" , "swish" , "swiss" , "swive" , "swoon" , "swoop" , "sword" , "swore" , "sworn" , "swung" , "sylph" , "synch" , "syncs" , "synod" , "syrup" , "tabby" , "table" , "taboo" , "tabor" , "tabus" , "tacet" , "tacit" , "tacks" , "tacky" , "tacos" , "tacts" , "taels" , "taffy" , "tagua" , "tails" , "taint" , "taken" , "taker" , "takes" , "talcs" , "tales" , "talks" , "talky" , "tally" , "talon" , "talus" , "tamed" , "tamer" , "tames" , "tamps" , "tango" , "tangs" , "tangy" , "tanks" , "tansy" , "taped" , "taper" , "tapes" , "tapir" , "tapis" , "tardy" , "tared" , "tares" , "tarns" , "taros" , "tarot" , "tarps" , "tarry" , "tarts" , "tasks" , "taste" , "tasty" , "tater" , "tatty" , "taunt" , "taupe" , "tawny" , "taxed" , "taxer" , "taxes" , "taxis" , "taxol" , "taxon" , "teach" , "teaks" , "teals" , "teams" , "tears" , "teary" , "tease" , "teats" , "techs" , "techy" , "tecum" , "teddy" , "teems" , "teens" , "teeny" , "teeth" , "telex" , "tells" , "telly" , "tempi" , "tempo" , "temps" , "tempt" , "tench" , "tends" , "tenet" , "tenon" , "tenor" }
    austin_words |= { "tense" , "tenth" , "tents" , "tepee" , "tepid" , "terce" , "terms" , "terns" , "terra" , "terry" , "terse" , "tesla" , "tests" , "testy" , "tetra" , "texas" , "texts" , "thane" , "thank" , "thanx" , "thats" , "thaws" , "thees" , "theft" , "their" , "theme" , "thens" , "there" , "therm" , "these" , "theta" , "thews" , "thick" , "thief" , "thigh" , "thine" , "thing" , "think" , "thins" , "third" , "thong" , "thorn" , "those" , "thous" , "three" , "threw" , "throb" , "throe" , "throw" , "thrum" , "thuds" , "thugs" , "thumb" , "thump" , "thunk" , "thwap" , "thyme" , "tiara" , "tibia" , "ticks" , "tidal" , "tided" , "tides" , "tiers" , "tiffs" , "tiger" , "tight" , "tikes" , "tikis" , "tilde" , "tiled" , "tiler" , "tiles" , "tills" , "tilth" , "tilts" , "timed" , "timer" , "times" , "timid" , "tines" , "tinge" , "tings" , "tinny" , "tints" , "tippy" , "tipsy" , "tired" , "tires" , "tiros" , "titan" , "titer" , "tithe" , "title" , "titre" , "tizzy" , "toads" , "toady" , "toast" , "today" , "toddy" , "toffs" , "toffy" , "togas" , "toile" , "toils" , "toked" , "token" , "toker" , "tokes" , "tolls" , "tombs" , "tomes" , "tommy" , "tonal" , "toned" , "toner" , "tones" , "tongs" , "tonic" , "tools" , "toons" , "tooth" , "toots" , "topaz" , "toped" , "toper" , "topes" , "topic" , "topoi" , "topos" , "toque" , "torah" , "torch" , "toric" , "torsi" , "torso" , "torte" , "torts" , "torus" , "total" , "toted" , "totem" , "toter" , "totes" , "totty" , "touch" , "tough" , "tours" , "touts" , "toves" , "towed" , "towel" , "tower" , "towns" , "toxic" , "toxin" , "toyed" , "toyer" , "toyon" , "trace" , "track" , "tract" , "trade" , "trail" , "train" , "trait" , "tramp" , "trams" , "trans" , "traps" , "trash" , "trawl" , "trays" , "tread" , "treap" , "treat" , "treed" , "trees" , "treks" , "trend" , "tress" , "trews" , "treys" , "triad" , "trial" , "tribe" , "tribs" , "trice" , "trick" , "tried" , "trier" , "tries" , "trike" , "trill" , "trims" , "trios" , "tripe" , "trips" , "trite" , "troll" , "tromp" , "troop" , "troth" , "trots" , "trout" , "trove" , "trows" , "truce" , "truck" , "trued" , "truer" , "trues" , "truly" , "trump" , "trunk" , "truss" , "trust" , "truth" , "tryst" , "tsars" , "tuans" , "tubal" , "tubas" , "tubby" , "tubed" , "tuber" , "tubes" , "tucks" , "tufas" , "tufts" , "tufty" , "tulip" , "tulle" , "tummy" , "tumor" , "tunas" , "tuned" , "tuner" , "tunes" , "tunic" , "tunny" , "tuple" , "turbo" , "turds" , "turdy" , "turfs" , "turfy" , "turns" , "turps" , "tusks" , "tusky" , "tutor" , "tutti" , "tutus" , "tuxes" , "twain" , "twang" , "twats" , "tweak" , "tweed" , "tweet" , "twerp" , "twice" , "twigs" , "twill" , "twine" , "twink" , "twins" , "twiny" , "twirl" , "twirp" , "twist" , "twits" , "twixt" , "tying" , "tykes" , "typal" , "typed" , "types" , "typos" , "tyres" , "tyros" , "tzars" , "udder" , "ukase" , "ulcer" , "ulnar" , "ulnas" , "ultra" , "umbel" , "umber" , "umbra" , "umiak" , "umped" , "umpty" , "unapt" , "unarc" , "unarm" , "unary" , "unate" , "unban" , "unbar" , "unbox" , "uncap" , "uncle" , "uncut" , "under" , "undid" , "undue" , "unfed" , "unfit" , "unfix" , "unhip" , "unhit" , "unify" , "union" , "unite" , "units" , "unity" , "unjam" , "unlit" , "unman" , "unmap" , "unmet" , "unpeg" , "unpin" , "unrig" , "unsay" , "unsee" , "unset" , "unsew" , "unsex" , "untie" , "until" , "unwed" , "unwon" , "unzip" , "upend" , "upped" , "upper" , "upset" , "urban" , "ureas" , "urged" , "urger" , "urges" , "urine" , "usage" , "users" , "usher" , "using" , "usual" , "usurp" , "usury" , "uteri" , "utero" , "utter" , "uvula" , "vacua" , "vacuo" , "vague" , "vagus" , "vails" , "vales" , "valet" , "valid" , "valor" , "value" , "valve" , "vamps" , "vaned" , "vanes" , "vapes" , "vapid" , "vapor" , "varia" , "vases" , "vault" , "vaunt" , "veals" , "veeps" , "veers" , "vegan" , "veils" , "veins" , "veiny" , "velar" , "velds" , "veldt" , "venal" , "vends" , "venom" , "vents" , "venue" , "verbs" , "verge" , "versa" , "verse" , "verso" , "verst" , "verve" , "vests" , "vetch" , "vexed" , "vexes" , "vials" , "viand" , "vibes" , "vicar" , "vices" , "video" , "viers" , "views" , "vigil" , "vigor" , "viler" , "villa" , "ville" , "villi" , "vinca" , "vined" , "vines" , "vinyl" , "viola" , "viols" , "viper" , "viral" , "vireo" , "vires" , "virus" , "visas" , "vised" , "vises" , "visit" , "visor" , "vista" , "vitae" , "vital" , "vitam" , "vitas" , "vitro" , "vivas" , "vivid" , "vivre" , "vixen" , "vizor" , "vocab" , "vocal" , "vodka" , "vogue" , "voice" , "voids" , "voila" , "voile" , "volts" , "vomit" , "voted" , "voter" , "votes" , "vouch" , "vowed" , "vowel" , "vower" , "voxel" , "vroom" , "vulva" , "vying" , "wacko" , "wacky" , "waded" , "wader" , "wades" , "wadis" , "wafer" , "wafts" , "waged" , "wager" , "wages" , "wagon" , "wahoo" , "waifs" , "wails" , "waist" , "waits" , "waive" , "waked" , "waken" , "waker" , "wakes" , "waled" , "wales" , "walks" , "walls" , "waltz" , "wands" , "waned" , "wanes" , "wanly" , "wanna" , "wanta" , "wants" , "wards" , "wares" , "warms" , "warns" , "warps" , "warts" , "warty" , "washy" , "wasps" , "waspy" , "wassa" , "waste" , "watch" , "water" , "watsa" , "watts" , "waved" , "waver" , "waves" , "waxed" , "waxen" , "waxer" , "waxes" , "wazoo" , "weald" , "weals" , "weans" , "wears" , "weary" , "weave" , "webby" , "weber" , "wedge" , "wedgy" , "weeds" , "weedy" , "weeks" , "weeny" , "weeps" , "weepy" , "weest" , "wefts" , "weigh" , "weird" , "weirs" , "welch" , "welds" , "wells" , "welsh" , "welts" , "wench" , "wends" , "wests" , "wetly" , "whack" , "whale" , "whams" , "whang" , "wharf" , "whats" , "wheal" , "wheat" , "wheee" , "wheel" , "whelk" , "whelm" , "whelp" , "whens" , "where" , "whets" , "whews" , "wheys" , "which" , "whiff" , "while" , "whims" , "whine" , "whiny" , "whips" , "whipt" , "whirl" , "whirr" , "whirs" , "whish" , "whisk" , "whist" , "white" , "whits" , "whizz" , "whoas" , "whole" , "whomp" , "whooo" , "whoop" , "whops" , "whore" , "whorl" , "whose" , "whoso" , "whump" , "wicks" , "widen" , "wider" , "widow" , "width" , "wield" , "wifey" , "wilco" , "wilds" , "wiled" , "wiles" , "wills" , "wilts" , "wimps" , "wimpy" , "wince" , "winch" , "winds" , "windy" , "wined" , "wines" , "winey" , "wings" , "winks" , "winos" , "wiped" , "wiper" , "wipes" , "wired" , "wirer" , "wires" , "wised" , "wiser" , "wises" , "wisps" , "wispy" , "wists" , "witch" , "withs" , "witty" , "wives" , "wizen" , "woken" , "wolds" , "woman" , "wombs" , "women" , "wonks" , "wonky" , "wonts" , "woods" , "woody" , "wooed" , "wooer" , "woofs" , "wools" , "wooly" , "woosh" , "woozy" , "words" , "wordy" , "works" , "world" , "worms" , "wormy" , "worry" , "worse" , "worst" , "worth" , "worts" , "would" , "wound" , "woven" , "wowed" , "wowee" , "wrack" , "wraps" , "wrath" , "wreak" , "wreck" , "wrens" , "wrest" , "wrier" , "wring" , "wrist" , "write" , "writs" , "wrong" , "wrote" , "wroth" , "wrung" , "wryer" , "wryly" , "wurst" , "xenon" , "xerox" , "xored" , "xylem" , "yacht" , "yahoo" , "yanks" , "yards" , "yarns" , "yawed" , "yawls" , "yawns" , "yawny" , "yawps" , "yearn" , "years" , "yeast" , "yecch" , "yella" , "yells" , "yelps" , "yenta" , "yerba" , "yeses" , "yield" , "yikes" , "yipes" , "yobbo" , "yodel" , "yogas" , "yogic" , "yogis" , "yoked" , "yokel" , "yokes" , "yolks" , "yolky" , "yores" , "young" , "yourn" , "yours" , "youse" , "youth" , "yowls" , "yoyos" , "yucca" , "yucky" , "yukky" , "yules" , "yummy" , "yurts" , "zappy" , "zayin" , "zeals" , "zebra" , "zebus" , "zeros" , "zests" , "zesty" , "zetas" , "zilch" , "zincs" , "zings" , "zingy" , "zippy" , "zloty" , "zombi" , "zonal" , "zoned" , "zones" , "zonks" , "zooey" , "zooks" , "zooms" , "zowie" }

    austin_words = list( austin_words )
    
    _clear_box( to_box )

    box[ to_box ].insert( "end" , "# #################################################################### #\n"   )
    box[ to_box ].insert( "end" , "#                               Notice:                                #\n"   )
    box[ to_box ].insert( "end" , "#    Wordlists were found on the internet. The internet may contain    #\n"   )
    box[ to_box ].insert( "end" , "#  offensive words. I removed some but am sure I did not get them all. #\n"   )
    box[ to_box ].insert( "end" , "# #################################################################### #\n\n" )

    ################################################
    ##                   Easy4                    ##
    ################################################

    cmnt = "Easy4" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    words = [ f'''{w.title()}''' for w in random.sample(list(austin_words),len(austin_words)) if len(w)==4 ]
    box[ to_box ].insert( "end" , "\n".join("  ".join("".join([ "".join(words.pop(0)for _ in range(3)),random.choice([r'!1',r'@2',r'#3',r'$4',r'%5',r'^6',r'&7',r'*8'])])for _ in range(4))for _ in range(8))+'\n\n')
    
    x="\n".join([ " ".join([random.choice( words )for _ in range(10)])for _ in range(8)])
    box[ to_box ].insert( "end" , f'{x}\n\n' )

    ################################################
    ##                   Easy5                    ##
    ################################################

    cmnt = "Easy5" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    words = [ f'''{w.title()}''' for w in random.sample(list(austin_words),len(austin_words)) if len(w)==5 ]
    box[ to_box ].insert( "end" , "\n".join("  ".join("".join([ "".join(words.pop(0)for _ in range(3)),random.choice([r'!1',r'@2',r'#3',r'$4',r'%5',r'^6',r'&7',r'*8'])])for _ in range(4))for _ in range(8))+'\n\n')

    x="\n".join([ " ".join([random.choice( words )for _ in range(10)])for _ in range(8)])
    box[ to_box ].insert( "end" , f'{x}\n\n' )

    ################################################
    ##          Non-Ambiguous Characters          ##
    ################################################

    cmnt = "Non-Ambiguous Characters" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    x="\n".join([ "  ".join([str(" ".join([ "".join([random.choice("2346789BCDFGHJKMPQRTVWXY")for _ in range(4)])for _ in range(8)])),str("".join([random.choice("2346789BCDFGHJKMPQRTVWXY")for _ in range(32)]))])for _ in range(8)])
    box[ to_box ].insert( "end" , f'{x}\n\n' )

    ################################################
    ##                 Lower Case                 ##
    ################################################
    
    cmnt = "Lower Case" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    x="\n".join([ "".join([random.choice("qpwoeirutyalskdjfhgzmxncbv")for _ in range(64)])for _ in range(8)])
    box[ to_box ].insert( "end" , f'{x}\n\n' )

    ################################################
    ##           Lower Case and Numbers           ##
    ################################################

    cmnt = "Lower Case and Numbers" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    x="\n".join([ "".join([random.choice("qpwoeirutyalskdjfhgzmxncbv0192837465")for _ in range(64)])for _ in range(8)])
    box[ to_box ].insert( "end" , f'{x}\n\n' )

    ################################################
    ##            Letters and Numbers             ##
    ################################################
    
    cmnt = "Letters and Numbers" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    x="\n".join([ "".join([random.choice("qpwoeirutyalskdjfhgzmxncbvZMXNCBVALSKDJFHGPQOWIEURYT0192837465")for _ in range(64)])for _ in range(8)])
    box[ to_box ].insert( "end" , f'{x}\n\n' )

    ################################################
    ##       Letters, Numbers, and Specials       ##
    ################################################

    cmnt = "Letters, Numbers, and Specials" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )
    x="\n".join([ "".join([random.choice(r'''qpwoeirutyalskdjfhgzmxncbvZMXNCBVALSKDJFHGPQOWIEURYT0192837465qpwoeirutyalskdjfhgzmxncbvZMXNCBVALSKDJFHGPQOWIEURYT0192837465!@#$%^&*''')for _ in range(64)])for _ in range(8)])
    box[ to_box ].insert( "end" , f'{x}\n\n' )

    #todo: cmnt = "DH passbook" ; box[ to_box ].insert( "end" , f'{"":#^48}\n## {cmnt:^42} ##\n{"":#^48}\n\n' )



# endregion  # Misc Functions ##########################################












########################################################################
#                             Execute Main                             #
########################################################################

# region     # Execute Main ############################################

if __name__ == '__main__' : main()

# endregion  # Execute Main ############################################



