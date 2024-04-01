#!/usr/bin/env python

# This is my Python Version my my ABC perl script.
# I made this before I knew Cyber Chef existed

# GitHub Description : Tool to replace command some basic command line functions. This version in Perl.
# GitHub Description : Tool to replace command some basic command line functions. This version in Python.

# https://github.com/HuskyCougar/abc.tk.py
# https://github.com/HuskyCougar/abc.tk.py.git
# git clone https://github.com/HuskyCougar/abc.tk.py.git







########################################################################
##                              Imports                               ##
########################################################################

# region     # Imports #################################################

import random
import datetime
import re
import os

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


def main() :

    build_main_window()
    menubar_file()
    menubar_abc()
    menubar_compare()
    menubar_tops()
    menubar_code()
    menubar_misc()
    menubar_options()

    abc[ "main_window" ].mainloop()

abc_window_title = "ABC - Python Version : 2024-04-01"
print( f'# INFO # {datetime.datetime.now():%Y-%m-%d %H:%M:%S} # Line : {getframeinfo(currentframe()).lineno:4,d} # Script Name : {getframeinfo(currentframe()).filename}' )
print( f'# INFO # {datetime.datetime.now():%Y-%m-%d %H:%M:%S} # Line : {getframeinfo(currentframe()).lineno:4,d} # Script Version : {abc_window_title}' )


# endregion  # Main Function ###########################################



####################################################################
##                        Build GUI Window                        ##
####################################################################

# region     ## Build GUI Window ###################################

def build_main_window() :

    abc[ "main_window" ] = Tk()

    abc[ "main_window" ].title( abc_window_title )
    #abc[ "main_window" ].title( "ABC - Python Version : 2024-03-23" )

    abc[ "main_window" ].option_add('*Dialog.msg.font', 'TkFixedFont')

    abc[ "Adjuster_LR" ] = PanedWindow( abc[ "main_window" ] , orient="horizontal" )

    abc[ "frame_L" ] = Frame( abc[ "main_window" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "frame_L" ].pack( side = "left" , fill = "both" , expand = True )
    abc[ "frame_R" ] = Frame( abc[ "main_window" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "frame_R" ].pack( side = "left" , fill = "both" , expand = True )

    abc[ "Adjuster_LR" ].add( abc[ "frame_L" ] )
    abc[ "Adjuster_LR" ].add( abc[ "frame_R" ] )
    abc[ "Adjuster_LR" ].pack( fill = "both" , expand = True )

    abc[ "Adjuster_AB" ] = PanedWindow( abc[ "frame_L" ] , orient = "vertical" )

    abc[ "frame_A" ] = Frame( abc[ "frame_L" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "frame_A" ].pack( side = "top" , fill = "both" , expand = "yes" )
    abc[ "frame_B" ] = Frame( abc[ "frame_L" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "frame_B" ].pack( side = "top" , fill = "both" , expand = "yes" )

    abc[ "Adjuster_AB" ].add( abc[ "frame_A" ] )
    abc[ "Adjuster_AB" ].add( abc[ "frame_B" ] )
    abc[ "Adjuster_AB" ].pack( fill = "both" , expand = True )

    abc[ "frame_C" ] = Frame( abc[ "frame_R" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "frame_C" ].pack( side = "top" , fill = "both" , expand = "yes" )

    abc[ "LabFrame_A" ] = LabelFrame( abc[ "frame_A" ] , text = "Box A" ) ; abc[ "LabFrame_A" ].pack( side = "top" , fill = "both" , expand = "yes" )
    abc[ "LabFrame_B" ] = LabelFrame( abc[ "frame_B" ] , text = "Box B" ) ; abc[ "LabFrame_B" ].pack( side = "top" , fill = "both" , expand = "yes" )
    abc[ "LabFrame_C" ] = LabelFrame( abc[ "frame_C" ] , text = "Box C" ) ; abc[ "LabFrame_C" ].pack( side = "top" , fill = "both" , expand = "yes" )

    abc[ "LabFrame_A_Top" ] = Frame( abc[ "LabFrame_A" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "LabFrame_A_Top" ].pack( side = "top" ,                expand = "no"  )
    abc[ "LabFrame_A_Bot" ] = Frame( abc[ "LabFrame_A" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "LabFrame_A_Bot" ].pack( side = "top" , fill = "both", expand = "yes" )

    abc[ "LabFrame_B_Top" ] = Frame( abc[ "LabFrame_B" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "LabFrame_B_Top" ].pack( side = "top" ,                expand = "no"  )
    abc[ "LabFrame_B_Bot" ] = Frame( abc[ "LabFrame_B" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "LabFrame_B_Bot" ].pack( side = "top" , fill = "both", expand = "yes" )

    abc[ "LabFrame_C_Top" ] = Frame( abc[ "LabFrame_C" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "LabFrame_C_Top" ].pack( side = "top" ,                expand = "no"  )
    abc[ "LabFrame_C_Bot" ] = Frame( abc[ "LabFrame_C" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "LabFrame_C_Bot" ].pack( side = "top" , fill = "both", expand = "yes" )

    box["A"] = ScrolledText( abc[ "LabFrame_A_Bot" ] , height = 15 , width = 60 , wrap = "none")
    box["B"] = ScrolledText( abc[ "LabFrame_B_Bot" ] , height = 15 , width = 60 , wrap = "none")
    box["C"] = ScrolledText( abc[ "LabFrame_C_Bot" ] , height = 15 , width = 60 , wrap = "none")

    abc[ "Button_A1" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'A  > B' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[ "Button_A2" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'A >> B' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[ "Button_A3" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'A <> B' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[ "Button_A4" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'A  > C' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[ "Button_A5" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'A >> C' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[ "Button_A6" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'A <> C' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[ "Button_A7" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'Dedupe' , command=lambda: _deduplicate_lines(    **{ "fm_box" : "A"                  } ) ).pack( side = "left" )
    abc[ "Button_A9" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'Sort'   , command=lambda: _sort_lines(           **{ "fm_box" : "A" , "order" : "A"  } ) ).pack( side = "left" )
    abc[ "Button_A8" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'Trim'   , command=lambda: _trim_blank_lines(     **{ "fm_box" : "A"                  } ) ).pack( side = "left" )
    abc[ "Button_AC" ] = Button( abc[ "LabFrame_A_Top" ] , text = 'Clear'  , command=lambda: _clear_box(                           "A"                    ) ).pack( side = "left" )

    abc[ "Button_B1" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'B  > A' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[ "Button_B2" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'B >> A' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[ "Button_B3" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'B <> A' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[ "Button_B4" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'B  > C' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[ "Button_B5" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'B >> C' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[ "Button_B6" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'B <> C' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ).pack( side = "left" )
    abc[ "Button_B7" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'Dedupe' , command=lambda: _deduplicate_lines(    **{ "fm_box" : "B"                  } ) ).pack( side = "left" )
    abc[ "Button_B9" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'Sort'   , command=lambda: _sort_lines(           **{ "fm_box" : "B" , "order" : "A"  } ) ).pack( side = "left" )
    abc[ "Button_B8" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'Trim'   , command=lambda: _trim_blank_lines(     **{ "fm_box" : "B"                  } ) ).pack( side = "left" )
    abc[ "Button_BC" ] = Button( abc[ "LabFrame_B_Top" ] , text = 'Clear'  , command=lambda: _clear_box(                           "B"                    ) ).pack( side = "left" )

    abc[ "Button_C1" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'C  > A' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[ "Button_C2" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'C >> A' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[ "Button_C3" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'C <> A' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ).pack( side = "left" )
    abc[ "Button_C4" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'C  > B' , command=lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[ "Button_C5" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'C >> B' , command=lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[ "Button_C6" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'C <> B' , command=lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ).pack( side = "left" )
    abc[ "Button_C7" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'Dedupe' , command=lambda: _deduplicate_lines(    **{ "fm_box" : "C"                  } ) ).pack( side = "left" )
    abc[ "Button_C9" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'Sort'   , command=lambda: _sort_lines(           **{ "fm_box" : "C" , "order" : "A"  } ) ).pack( side = "left" )
    abc[ "Button_C8" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'Trim'   , command=lambda: _trim_blank_lines(     **{ "fm_box" : "C"                  } ) ).pack( side = "left" )
    abc[ "Button_CC" ] = Button( abc[ "LabFrame_C_Top" ] , text = 'Clear'  , command=lambda: _clear_box(                           "C"                    ) ).pack( side = "left" )

    box["A"].pack( fill = "both" , expand = True )
    box["B"].pack( fill = "both" , expand = True )
    box["C"].pack( fill = "both" , expand = True )

    ## Frame with File A and File B ########################################

    #abc[ "frame_F" ] = Frame( abc[ "main_window" ] , relief = 'groove' , borderwidth = 1 ) ; abc[ "frame_F" ].pack( side = "bottom" , fill = "x" , expand = False )
    #
    #abc[ "LabFrame_FA" ] = LabelFrame( abc[ "frame_F" ] , text = "File A" )
    #abc[ "LabFrame_FB" ] = LabelFrame( abc[ "frame_F" ] , text = "File B" )
    #
    #abc[ "Button_FA" ] = Button(       abc[ "LabFrame_FA" ] , height = 2 , text = 'File Select' , command = lambda: _file_box_set( "Button_FA" , "File_A" ) )
    #box[ "File_A"    ] = ScrolledText( abc[ "LabFrame_FA" ] , height = 2 )
    #
    #abc[ "Button_FB" ] = Button(       abc[ "LabFrame_FB" ] , height = 2 , text = 'File Select' , command = lambda: _file_box_set( "Button_FB" , "File_B" ) )
    #box[ "File_B"    ] = ScrolledText( abc[ "LabFrame_FB" ] , height = 2 )
    #
    #abc[ "LabFrame_FA" ].pack( side = "left" , fill = "x" , expand = False )
    #abc[ "LabFrame_FB" ].pack( side = "left" , fill = "x" , expand = False )
    #
    #abc[ "Button_FA" ].pack( side = "left" )
    #abc[ "Button_FB" ].pack( side = "left" )
    #
    #box[ "File_A" ].pack( side = "left" , fill = "x" , expand = False )
    #box[ "File_B" ].pack( side = "left" , fill = "x" , expand = False )

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
    messagebox.showinfo( 'Well, shucks.' , 'This function is not done yet.' )


def _get_from_box( **kwargs ) :

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

    if lopts[ "record_separator" ] == "singlespace" : fm_lst = _data.splitlines()
    if lopts[ "record_separator" ] == "doublespace" : pass
    if lopts[ "record_separator" ] == "whitespace"  : fm_lst = fm_str.split( " " )

    if lopts[ "trim_leading_spaces"  ] : fm_lst = [ x.lstrip(" ") for x in fm_lst ]
    if lopts[ "trim_trailing_spaces" ] : fm_lst = [ x.rstrip(" ") for x in fm_lst ]
    if lopts[ "trim_blank_lines"     ] : fm_lst = [ x for x in _data if x.strip() ]

    #todo use this

    # return xxxxxx #


def _clear_box( _box ) : box[ _box ].delete( "1.0" , "end" )


def _clear_boxes( ) :
    box[ "A" ].delete( "1.0" , "end" )
    box[ "B" ].delete( "1.0" , "end" )
    box[ "C" ].delete( "1.0" , "end" )


def _Apnd_from_File( to_box ) : pass
def _Open_from_Clip( to_box ) : pass
def _Apnd_from_Clip( to_box ) : pass
def _Save_to_File(   fm_box ) : pass
def _Apnd_to_File(   fm_box ) : pass
def _Save_to_Clip(   fm_box ) : pass
def _Apnd_to_Clip(   fm_box ) : pass


def _folder_picker( to_box ) :

    '''Not Done. Not Used'''

    print( f'_file_picker( "{to_box}" )')

    file_get = rf'{filedialog.askdirectory(title="Select Folder")}'


def _Open_from_File( to_box , to_clear ) :

    print( f'_Open_from_File( "{to_box}" , "{to_clear}" )')

    file_get = rf'{filedialog.askopenfilename( title="Select One File" , filetypes=(("Text Files", "*.txt *.log *.json *.jsonl *.ndjson *.jsonld *.xml *.csv"),("Scripts", "*.pl *.rb *.py *.sh *.css *.js *.htm *.html"),("All Files", "*.*")))}'
    
    if not os.path.isfile( file_get ) :

        print( f'# ERR  # _Open_from_File # isfile fail : {file_get}' )
        messagebox.showinfo( f'# ERR  # _Open_from_File # isfile fail : {file_get}' )
    
    else :

        if to_clear : _clear_box( to_box )

        if   file_get.endswith( ".gz" ) : fh = gzip.open( file_get , "rb" )
        else                            : fh =      open( file_get , "r"  )

        box[ to_box ].insert( "end" , "".join( fh.readlines() ) )


def _file_box_set( to_parent , to_box ) :

    #todo : finish
    '''
    File select dialoge. Does not open files. Only gets file paths and 
    sets them in FileA or FileB for futute use through another get 
    function.
    '''

    print( f'_file_box_set( "{to_parent}" , "{to_box}" )')

    file_mget = rf'{filedialog.askopenfilename( parent=abc[ to_parent ] , title="Select One or More Files" , multiple = True , filetypes=(("Text Files", "*.txt *.log *.json *.jsonl *.ndjson *.jsonld *.xml *.csv"),("Scripts", "*.pl *.rb *.py *.sh *.css *.js *.htm *.html"),("All Files", "*.*")))}'

    print( f'_file_box_set file_mget( "{file_mget}" )')

    if file_mget : print( f'_file_box_set file_mget( "{file_mget}" )')
    if file_mget : print( f'_file_box_set type( "{type(file_mget)}" )')
    if file_mget : print( f'_file_box_set file_mget.split( "{file_mget.split()}" )')

    if file_mget :
        for x in re.findall( r'\'(..*?)\'', file_mget ) :
            if x and x.strip() : print( f'{x}' )


def _file_box_get( to_parent , to_box ) : pass


def _trim_blank_lines( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'_trim_blank_lines( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    to_box = fm_box

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()
    lst_fm = [ x.strip() for x in lst_fm if x.strip() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _trim_trailing_spaces( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'_trim_trailing_spaces( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.rstrip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _trim_leading_spaces( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'_trim_leading_spaces( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.lstrip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _deduplicate_lines( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )
    #todo: Maintain order

    print( f'_deduplicate_lines( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    set_fm     = set()
    set_fm_add = set_fm.add

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

    lst_fm = [ x for x in lst_fm if not ( x in set_fm or set_fm_add( x ) ) ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _sort_lines( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )
    order  = kwargs.get( "order"  , "A" )

    print( f'_sort_lines( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" , "order" : "{order}" }} )' )

    if order == "A" : lst_fm = sorted( box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() )
    if order == "D" : lst_fm = sorted( box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() , reverse=True )

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _change_case_upper( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'_change_case_upper( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.upper() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _change_case_lower( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'_change_case_lower( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.lower() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _change_case_casefold( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'_change_case_casefold( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.casefold() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _change_case_title( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , fm_box )

    print( f'_change_case_title( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = [ x.title() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    _clear_box( to_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _apnd_to_box_from_box( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , "C" )

    print( f'_apnd_to_box_from_box( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

    #_clear_box( fm_box )

    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _swap_to_box_from_box( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , "C" )

    print( f'_swap_to_box_from_box( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

    lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()
    lst_to = box[ to_box ].get( "1.0" , 'end-1c' ).splitlines()

    _clear_box( fm_box )
    _clear_box( to_box )

    for x in lst_to : box[ fm_box ].insert( "end" , f"{x}\n" )
    for x in lst_fm : box[ to_box ].insert( "end" , f"{x}\n" )


def _move_to_box_from_box( **kwargs ) :

    fm_box = kwargs.get( "fm_box" , "A" )
    to_box = kwargs.get( "to_box" , "C" )

    print( f'_move_to_box_from_box( {{ "fm_box" : "{fm_box}" , "to_box" : "{to_box}" }} )' )

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

def menubar_file() :

    ## Main Title Menu #################################################

    abc[ "menubar" ] = Menu( abc[ "main_window" ] )

    abc[ "main_window" ].config( menu = abc[ "menubar" ] )

    ####################################################################
    #                            File Menu                             #
    ####################################################################

    abc[ "menubar_file" ] = Menu( abc[ "menubar" ] , tearoff = 1 ) ; abc[ "menubar" ].add_cascade( label = "File" , menu = abc[ "menubar_file" ] )

    abc[ "menubar_file" ].add_command( label = 'Exit' , command = abc[ "main_window" ].destroy )

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

def menubar_options() :

    abc[ "menubar_options"  ] = Menu( abc[ "menubar" ] , tearoff = 1 ) ; abc[ "menubar" ].add_cascade( label = "Options"   , menu = abc[ "menubar_options"  ] )

    ## Options Menu : Default Record Separators ########################

    abc[ "options_record_separator" ] = StringVar()
    abc[ "options_record_separator" ].set( gopts[ "record_separator" ] )

    abc[ "menubar_options_rec_sep"  ] = Menu( abc[ "menubar_options" ] , tearoff = 1 )

    abc[ "menubar_options" ].add_cascade( font = "TkFixedFont" , label = "Default Record Separator" , menu = abc[ "menubar_options_rec_sep" ] )

    abc[ "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Newline         \\n"            , value = '\n'       , variable=abc[ "options_record_separator" ] )
    abc[ "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "CRLF            \\r\\n"         , value = '\r\n'     , variable=abc[ "options_record_separator" ] )
    abc[ "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Double Newline  \\n\\n"         , value = '\n\n'     , variable=abc[ "options_record_separator" ] )
    abc[ "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Double CRLF     \\r\\n\\r\\n"   , value = '\r\n\r\n' , variable=abc[ "options_record_separator" ] )
    abc[ "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Pound LF        #\\n"           , value = '#\n'      , variable=abc[ "options_record_separator" ] )
    abc[ "menubar_options_rec_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Bang LF         !\\n"           , value = '!\n'      , variable=abc[ "options_record_separator" ] )

    ## Options Menu : Default Column Separator #########################

    abc[ "options_column_separator" ] = StringVar()
    abc[ "options_column_separator" ].set( gopts[ "column_separator" ] )

    abc[ "menubar_options_col_sep"  ] = Menu( abc[ "menubar_options" ] , tearoff = 1 )

    abc[ "menubar_options" ].add_cascade( font = "TkFixedFont" , label = "Default Column Separator" , menu = abc[ "menubar_options_col_sep" ] )

    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Comma           \",\""     , value = ','     , variable=abc[ "options_column_separator" ] )
    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Comma Space     \", \""    , value = ', '    , variable=abc[ "options_column_separator" ] )
    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Pipe            \"|\""     , value = '|'     , variable=abc[ "options_column_separator" ] )
    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Carat           \"^\""     , value = '^'     , variable=abc[ "options_column_separator" ] )
    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Spaced ORs      \" OR \""  , value = ' OR '  , variable=abc[ "options_column_separator" ] )
    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Spaced ||s      \" || \""  , value = ' OR '  , variable=abc[ "options_column_separator" ] )
    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Spaced ANDs     \" AND \"" , value = ' AND ' , variable=abc[ "options_column_separator" ] )
    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Spaced &&s      \" && \""  , value = ' AND ' , variable=abc[ "options_column_separator" ] )
    abc[ "menubar_options_col_sep"  ].add_radiobutton( font = "TkFixedFont" , label = "Cherries        \"@@@\""   , value = '@@@'   , variable=abc[ "options_column_separator" ] )

    ## Options Menu : Readlines Options ################################

    abc[ "options_trim_leading_spaces"  ] = BooleanVar()
    abc[ "options_trim_trailing_spaces" ] = BooleanVar()
    abc[ "options_trim_blank_lines"     ] = BooleanVar()
    abc[ "options_read_in_boxes_upper"  ] = BooleanVar()
    abc[ "options_read_in_boxes_lower"  ] = BooleanVar()
    abc[ "options_read_in_boxes_dedupe" ] = BooleanVar()

    abc[ "options_trim_leading_spaces"  ].set( gopts[ "trim_leading_spaces"  ] )
    abc[ "options_trim_trailing_spaces" ].set( gopts[ "trim_trailing_spaces" ] )
    abc[ "options_trim_blank_lines"     ].set( gopts[ "trim_blank_lines"     ] )
    abc[ "options_read_in_boxes_upper"  ].set( gopts[ "read_in_boxes_upper"  ] )
    abc[ "options_read_in_boxes_lower"  ].set( gopts[ "read_in_boxes_lower"  ] )
    abc[ "options_read_in_boxes_dedupe" ].set( gopts[ "read_in_boxes_dedupe" ] )

    abc[ "menubar_options"  ].add_checkbutton( label = "Trim leading spaces on read"  , onvalue=1 , offvalue=0 , variable=abc[ "options_trim_leading_spaces"  ] )
    abc[ "menubar_options"  ].add_checkbutton( label = "Trim trailing spaces on read" , onvalue=1 , offvalue=0 , variable=abc[ "options_trim_trailing_spaces" ] )
    abc[ "menubar_options"  ].add_checkbutton( label = "Trim blank lines on read"     , onvalue=1 , offvalue=0 , variable=abc[ "options_trim_blank_lines"     ] )
    abc[ "menubar_options"  ].add_checkbutton( label = "Uppercase on read"            , onvalue=1 , offvalue=0 , variable=abc[ "options_read_in_boxes_upper"  ] )
    abc[ "menubar_options"  ].add_checkbutton( label = "Lowercase on read"            , onvalue=1 , offvalue=0 , variable=abc[ "options_read_in_boxes_lower"  ] )
    abc[ "menubar_options"  ].add_checkbutton( label = "Dedupe on read"               , onvalue=1 , offvalue=0 , variable=abc[ "options_read_in_boxes_dedupe" ] )

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

def menubar_abc() :

    abc[ "menubar_abc" ] = Menu( abc[ "menubar" ] , tearoff = 1 )
    
    abc[ "menubar" ].add_cascade( label = "ABC" , menu = abc[ "menubar_abc" ] )

    abc[ "menubar_abc" ].add_command( font = "TkFixedFont" , label = 'Clear All Boxes' , command = lambda: _clear_boxes() )
    abc[ "menubar_abc" ].add_command( font = "TkFixedFont" , label = 'Clear Box A'     , command = lambda: _clear_box( "A" ) )
    abc[ "menubar_abc" ].add_command( font = "TkFixedFont" , label = 'Clear Box B'     , command = lambda: _clear_box( "B" ) )
    abc[ "menubar_abc" ].add_command( font = "TkFixedFont" , label = 'Clear Box C'     , command = lambda: _clear_box( "C" ) )

    abc[ "menubar_abc" ].add_separator()

    ####################################################################
    ##                        ABC Menu: Box A                         ##
    ####################################################################

    abc[ "menubar_abc__box_a"  ] = Menu( abc[ "menubar_abc" ] , tearoff = 1 )

    abc[ "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box A" , menu = abc[ "menubar_abc__box_a" ] )

    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Open File into Box'               , command = lambda: _Open_from_File( "A" , 1 ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Open File Append to Box'          , command = lambda: _Open_from_File( "A" , 0 ) )
    #abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Save to File'                     , command = lambda: _not_done_yet() )
    #abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Append to File'                   , command = lambda: _not_done_yet() )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Sort lines ascending order'       , command = lambda: _sort_lines(           **{ "fm_box" : "A" , "to_box" : "A" , "order" : "A" } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Sort lines descending order'      , command = lambda: _sort_lines(           **{ "fm_box" : "A" , "to_box" : "A" , "order" : "D" } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Dedupe Lines'                     , command = lambda: _deduplicate_lines(    **{ "fm_box" : "A"                  } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Trim blank lines and spaces'      , command = lambda: _trim_blank_lines(     **{ "fm_box" : "A"                  } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Trim trailing whitespace'         , command = lambda: _trim_trailing_spaces( **{ "fm_box" : "A"                  } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Trim leading whitespace'          , command = lambda: _trim_leading_spaces(  **{ "fm_box" : "A"                  } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Change data to upper case'        , command = lambda: _change_case_upper(    **{ "fm_box" : "A"                  } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Change data to lower case'        , command = lambda: _change_case_lower(    **{ "fm_box" : "A"                  } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Change data to casefold case'     , command = lambda: _change_case_casefold( **{ "fm_box" : "A"                  } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Change data to title case'        , command = lambda: _change_case_title(    **{ "fm_box" : "A"                  } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Swap Box A contents with Box B'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Swap Box A contents with Box C'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Move Box A contents to Box B'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Move Box A contents to Box C'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Append Box A contents to Box B'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Append Box A contents to Box C'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) )
    abc[ "menubar_abc__box_a" ].add_command( font = "TkFixedFont" , label = 'Clear Box'                        , command = lambda: _clear_box(                           "A"                    ) )

    ####################################################################
    ##                        ABC Menu: Box B                         ##
    ####################################################################

    abc[ "menubar_abc__box_b"  ] = Menu( abc[ "menubar_abc" ] , tearoff = 1 )

    abc[ "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box B" , menu = abc[ "menubar_abc__box_b" ] )

    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Open File into Box'               , command = lambda: _Open_from_File( "B" , 1 ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Open File Append to Box'          , command = lambda: _Open_from_File( "B" , 0 ) )
    #abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Save to File'                     , command = lambda: _not_done_yet() )
    #abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Append to File'                   , command = lambda: _not_done_yet() )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Sort lines ascending order'       , command = lambda: _sort_lines(           **{ "fm_box" : "B" , "to_box" : "B" , "order" : "A" } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Sort lines descending order'      , command = lambda: _sort_lines(           **{ "fm_box" : "B" , "to_box" : "B" , "order" : "D" } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Dedupe Lines'                     , command = lambda: _deduplicate_lines(    **{ "fm_box" : "B"                  } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Trim blank lines and spaces'      , command = lambda: _trim_blank_lines(     **{ "fm_box" : "B"                  } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Trim trailing whitespace'         , command = lambda: _trim_trailing_spaces( **{ "fm_box" : "B"                  } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Trim leading whitespace'          , command = lambda: _trim_leading_spaces(  **{ "fm_box" : "B"                  } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Change data to upper case'        , command = lambda: _change_case_upper(    **{ "fm_box" : "B"                  } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Change data to lower case'        , command = lambda: _change_case_lower(    **{ "fm_box" : "B"                  } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Change data to casefold case'     , command = lambda: _change_case_casefold( **{ "fm_box" : "B"                  } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Change data to title case'        , command = lambda: _change_case_title(    **{ "fm_box" : "B"                  } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Swap Box B contents with Box A'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Swap Box B contents with Box C'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Move Box B contents to Box A'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Move Box B contents to Box C'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Append Box B contents to Box A'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Append Box B contents to Box C'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) )
    abc[ "menubar_abc__box_b" ].add_command( font = "TkFixedFont" , label = 'Clear Box'                        , command = lambda: _clear_box(                           "B"                    ) )

    ####################################################################
    ##                        ABC Menu: Box C                         ##
    ####################################################################

    abc[ "menubar_abc__box_c"  ] = Menu( abc[ "menubar_abc" ] , tearoff = 1 )

    abc[ "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box C" , menu = abc[ "menubar_abc__box_c" ] )

    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Open File into Box'               , command = lambda: _Open_from_File( "C" , 1 ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Open File Append to Box'          , command = lambda: _Open_from_File( "C" , 0 ) )
    #abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Save to File'                     , command = lambda: _not_done_yet() )
    #abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Append to File'                   , command = lambda: _not_done_yet() )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Sort lines ascending order'       , command = lambda: _sort_lines(           **{ "fm_box" : "C" , "to_box" : "C" , "order" : "A" } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Sort lines descending order'      , command = lambda: _sort_lines(           **{ "fm_box" : "C" , "to_box" : "C" , "order" : "D" } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Dedupe Lines'                     , command = lambda: _deduplicate_lines(    **{ "fm_box" : "C"                  } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Trim blank lines and spaces'      , command = lambda: _trim_blank_lines(     **{ "fm_box" : "C"                  } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Trim trailing whitespace'         , command = lambda: _trim_trailing_spaces( **{ "fm_box" : "C"                  } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Trim leading whitespace'          , command = lambda: _trim_leading_spaces(  **{ "fm_box" : "C"                  } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Change data to upper case'        , command = lambda: _change_case_upper(    **{ "fm_box" : "C"                  } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Change data to lower case'        , command = lambda: _change_case_lower(    **{ "fm_box" : "C"                  } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Change data to casefold case'     , command = lambda: _change_case_casefold( **{ "fm_box" : "C"                  } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Change data to title case'        , command = lambda: _change_case_title(    **{ "fm_box" : "C"                  } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Swap Box C contents with Box A'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Swap Box C contents with Box B'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Move Box C contents to Box A'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Move Box C contents to Box B'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Append Box C contents to Box A'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Append Box C contents to Box B'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) )
    abc[ "menubar_abc__box_c" ].add_command( font = "TkFixedFont" , label = 'Clear Box'                        , command = lambda: _clear_box(                           "C"                    ) )

    ####################################################################
    ##                       ABC Menu: Box Swap                       ##
    ####################################################################

    abc[ "menubar_abc__swap"   ] = Menu( abc[ "menubar_abc" ] , tearoff = 1 )

    abc[ "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box Swap" , menu = abc[ "menubar_abc__swap" ] )

    abc[ "menubar_abc__swap"   ].add_command( font = "TkFixedFont" , label = 'Swap Box A contents with Box B'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_swap("A" , "B")   ; } ]
    abc[ "menubar_abc__swap"   ].add_command( font = "TkFixedFont" , label = 'Swap Box A contents with Box C'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_swap("A" , "C")   ; } ]
    abc[ "menubar_abc__swap"   ].add_command( font = "TkFixedFont" , label = 'Swap Box B contents with Box A'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_swap("B" , "A")   ; } ]
    abc[ "menubar_abc__swap"   ].add_command( font = "TkFixedFont" , label = 'Swap Box B contents with Box C'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_swap("B" , "C")   ; } ]
    abc[ "menubar_abc__swap"   ].add_command( font = "TkFixedFont" , label = 'Swap Box C contents with Box A'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_swap("C" , "A")   ; } ]
    abc[ "menubar_abc__swap"   ].add_command( font = "TkFixedFont" , label = 'Swap Box C contents with Box B'   , command = lambda: _swap_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_swap("C" , "B")   ; } ]

    ####################################################################
    ##                       ABC Menu: Box Move                       ##
    ####################################################################

    abc[ "menubar_abc__move"   ] = Menu( abc[ "menubar_abc" ] , tearoff = 1 )

    abc[ "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box Move" , menu = abc[ "menubar_abc__move"   ] )

    abc[ "menubar_abc__move"   ].add_command( font = "TkFixedFont" , label = 'Move Box A contents to Box B'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_move("A" , "B")   ; } ]
    abc[ "menubar_abc__move"   ].add_command( font = "TkFixedFont" , label = 'Move Box A contents to Box C'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_move("A" , "C")   ; } ]
    abc[ "menubar_abc__move"   ].add_command( font = "TkFixedFont" , label = 'Move Box B contents to Box A'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_move("B" , "A")   ; } ]
    abc[ "menubar_abc__move"   ].add_command( font = "TkFixedFont" , label = 'Move Box B contents to Box C'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_move("B" , "C")   ; } ]
    abc[ "menubar_abc__move"   ].add_command( font = "TkFixedFont" , label = 'Move Box C contents to Box A'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_move("C" , "A")   ; } ]
    abc[ "menubar_abc__move"   ].add_command( font = "TkFixedFont" , label = 'Move Box C contents to Box B'     , command = lambda: _move_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_move("C" , "B")   ; } ]

    ####################################################################
    ##                      ABC Menu: Box Append                      ##
    ####################################################################

    abc[ "menubar_abc__apnd"   ] = Menu( abc[ "menubar_abc" ] , tearoff = 1 )

    abc[ "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "Box Append" , menu = abc[ "menubar_abc__apnd" ] )

    abc[ "menubar_abc__apnd"   ].add_command( font = "TkFixedFont" , label = 'Append Box A contents to Box B'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_append("A" , "B")  ; } ]
    abc[ "menubar_abc__apnd"   ].add_command( font = "TkFixedFont" , label = 'Append Box A contents to Box C'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "A" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_append("A" , "C")  ; } ]
    abc[ "menubar_abc__apnd"   ].add_command( font = "TkFixedFont" , label = 'Append Box B contents to Box A'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_append("B" , "A")  ; } ]
    abc[ "menubar_abc__apnd"   ].add_command( font = "TkFixedFont" , label = 'Append Box B contents to Box C'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "B" , "to_box" : "C" } ) ) #   -command => sub { &U__ABC__data_append("B" , "C")  ; } ]
    abc[ "menubar_abc__apnd"   ].add_command( font = "TkFixedFont" , label = 'Append Box C contents to Box A'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "A" } ) ) #   -command => sub { &U__ABC__data_append("C" , "A")  ; } ]
    abc[ "menubar_abc__apnd"   ].add_command( font = "TkFixedFont" , label = 'Append Box C contents to Box B'   , command = lambda: _apnd_to_box_from_box( **{ "fm_box" : "C" , "to_box" : "B" } ) ) #   -command => sub { &U__ABC__data_append("C" , "B")  ; } ]

    # ####################################################################
    # ##                        ABC Menu: File A                        ##
    # ####################################################################
    # 
    # abc[ "menubar_abc__file_a" ] = Menu( abc[ "menubar_abc" ] , tearoff = 1 )
    # 
    # abc[ "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "File A" , menu = abc[ "menubar_abc__file_a" ] )
    # 
    # abc[ "menubar_abc__file_a" ].add_command( font = "TkFixedFont" , label = 'Append File A and File B to Box A' , command = lambda: _not_done_yet() )
    # abc[ "menubar_abc__file_a" ].add_command( font = "TkFixedFont" , label = 'Diff File A and File B to Box C'   , command = lambda: _not_done_yet() )
    # 
    # ####################################################################
    # ##                        ABC Menu: File B                        ##
    # ####################################################################
    # 
    # abc[ "menubar_abc__file_b" ] = Menu( abc[ "menubar_abc" ] , tearoff = 1 )
    # 
    # abc[ "menubar_abc" ].add_cascade( font = "TkFixedFont" , label = "File B" , menu = abc[ "menubar_abc__file_b"   ] )
    # 
    # abc[ "menubar_abc__file_b" ].add_command( font = "TkFixedFont" , label = 'Append File A and File B to Box A' , command = lambda: _not_done_yet() )
    # abc[ "menubar_abc__file_b" ].add_command( font = "TkFixedFont" , label = 'Diff File A and File B to Box C'   , command = lambda: _not_done_yet() )

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

def menubar_compare(): 

    abc[ "menubar_compare" ] = Menu( abc[ "menubar" ] , tearoff = 1 ) ; abc[ "menubar" ].add_cascade( label = "Compare"   , menu = abc[ "menubar_compare"  ] )

    abc[ "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'A + B to C (Merge A and B)'                 , command = lambda: abc__compare__AB_union(     "A" , "B" , "C" ) )
    abc[ "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'A - B to C (Take B from A)'                 , command = lambda: abc__compare__AB_minus(     "A" , "B" , "C" ) )
    abc[ "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'B - A to C (Take A from B)'                 , command = lambda: abc__compare__AB_minus(     "B" , "A" , "C" ) )
    abc[ "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'AB to C (In both A and B)'                  , command = lambda: abc__compare__AB_intersect( "A" , "B" , "C" ) )
    abc[ "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'A + B - AB to C (In A or B but not both)'   , command = lambda: abc__compare__AB_symdiff(   "A" , "B" , "C" ) )
    abc[ "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'Labeled Diff A and B'                       , command = lambda: abc__compare__AB_diff(      "A" , "B" , "C" ) )
    abc[ "menubar_compare" ].add_command( font = "TkFixedFont" , label = 'Count Lines in Each Box'                    , command = lambda: abc__cardinality_all() )

    ####################################################################

    abc[ "menubar_compare" ].add_separator()

    ####################################################################

    abc[ "menubar_compare__more"  ] = Menu( abc[ "menubar_compare" ] , tearoff = 1 )

    abc[ "menubar_compare" ].add_cascade( font = "TkFixedFont" , label = "More" , menu = abc[ "menubar_compare__more"  ] )

    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = 'A & B                 > Box C' , command = lambda: abc__compare__AB_union(     "A" , "B" , "C" ) )
    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = 'A - B                 > Box C' , command = lambda: abc__compare__AB_minus(     "A" , "B" , "C" ) )
    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = 'B - A                 > Box C' , command = lambda: abc__compare__AB_minus(     "B" , "A" , "C" ) )
    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = 'A | B                 > Box C' , command = lambda: abc__compare__AB_intersect( "A" , "B" , "C" ) )
    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = 'A \u0394 B = ( A - B ) & ( B - A )  > Box C' , command = lambda: abc__compare__AB_symdiff(   "A" , "B" , "C" ) )
    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = 'A X B (Cross Product) > Box C' , command = lambda: abc__compare__AB_cross_prod( "A" , "B" , "C" ) )
    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = '|A|         '                  , command = lambda: abc__cardinality_one( "A" ) )
    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = '|B|         '                  , command = lambda: abc__cardinality_one( "B" ) )
    abc[ "menubar_compare__more"  ].add_command( font = "TkFixedFont" , label = '|C|         '                  , command = lambda: abc__cardinality_one( "C" ) )

# endregion  ## Compare Menu ###########################################

########################################################################
#                          Compare Functions                           #
########################################################################

# region     # Compare Functions #######################################

# set_a | set_b  # Union
# set_a & set_b  # Intersection
# set_a - set_b  # Diff
# set_b - set_a  # Diff
# set_b ^ set_a  # Unique elements in each set. symetric difference

def abc__compare__AB_union( box_a , box_b , to_box ) :

    print( f'abc__compare__AB_union( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )

    for x in set_a.union( set_b ) :
        if x and x.strip() : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__compare__AB_intersect( box_a , box_b , to_box ) :

    print( f'abc__compare__AB_intersect( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )

    for x in set_a.intersection( set_b ) :
        if x and x.strip() : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__compare__AB_minus( box_a , box_b , to_box ) :

    print( f'abc__compare__AB_minus( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )

    for x in set_a.difference( set_b ) :
        if x and x.strip() : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__compare__AB_diff( box_a , box_b , to_box ) :  # todo : make a proper diff

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


def abc__compare__AB_symdiff( box_a , box_b , to_box ) :

    print( f'abc__compare__AB_symdiff( "{box_a}" , "{box_b}" , "{to_box}" )')

    set_a = set( [ x.strip() for x in box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )
    set_b = set( [ x.strip() for x in box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ] )

    _clear_box( to_box )

    for x in set_a.symmetric_difference( set_b ) :
        if x and x.strip() : box[ to_box ].insert( "end" , f"{x}\n" )


def abc__cardinality_one( fm_box ):

    print( f'abc__cardinality_one( "{fm_box}" )')

    lst_a = [ x.strip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() if x.strip() ]

    messagebox.showinfo( 'Cardinality' , f'{len( lst_a ):14,d} : Total lines in Box {fm_box}\n{len( set( lst_a ) ):14,d} : Total unique lines in Box {fm_box}' )


def abc__cardinality_all( ):

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


def abc__compare__AB_cross_prod( box_a , box_b , to_box ) :

    set_a = set( box[ box_a ].get( "1.0" , 'end-1c' ).splitlines() )
    set_b = set( box[ box_b ].get( "1.0" , 'end-1c' ).splitlines() )

    column_separator = gopts[ "column_separator" ]

    _clear_box( to_box )

    for v1 , v2 in [ ( x , y ) for x in set_a for y in set_b ] :
        box[ to_box ].insert( "end" , f"{v1}{column_separator}{v2}\n" )


def U__compare__A_minus_BorC() : pass


def U__compare__A_minus_BandC() : pass


def U__compare__AorB_minus_C() : pass


def U__compare__AandB_minus_C() : pass


def U__compare__A_and_BorC() : pass


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

def menubar_tops() :

    abc[ "menubar_tops"     ] = Menu( abc[ "menubar" ] , tearoff = 1 ) ; abc[ "menubar" ].add_cascade( label = "Text Ops" , menu = abc[ "menubar_tops"     ] )

    ####################################################################
    ##              Text Ops Menu : Basic Bash Commands               ##
    ####################################################################

    abc[ "menubar_tops"   ].add_command( font = "TkFixedFont" , label = 'sort (A) and unique (C)'                           , command = lambda: abc__tops__sort_unique(            "A" , "C" ) )
    abc[ "menubar_tops"   ].add_command( font = "TkFixedFont" , label = 'sort (A), unique and count (C)'                    , command = lambda: abc__tops__sort_unique_count(      "A" , "C" ) )
    abc[ "menubar_tops"   ].add_command( font = "TkFixedFont" , label = 'sort (A), unique, count and sort again (C)'        , command = lambda: abc__tops__sort_unique_count_sort( "A" , "C" ) )
    abc[ "menubar_tops"   ].add_command( font = "TkFixedFont" , label = 'Split lines from (A) into n line groups (C)'       , command = lambda: abc__tops__split_by_n_lines( "A" , "C" ) )
    abc[ "menubar_tops"   ].add_command( font = "TkFixedFont" , label = 'Shuffle lines (A) to (C)'                          , command = lambda: abc__tops__randomize_list(   "A" , "C" ) )
    abc[ "menubar_tops"   ].add_command( font = "TkFixedFont" , label = 'String Interpolate (B) using vars in (A) to to (C)' , command = lambda: abc__tops__string_interpolate( "A" , "B" , "C" ) )

    ####################################################################
    ##                Text Ops Menu : Extract Columns                 ##
    ####################################################################

    ####################################################################
    ##                  Text Ops Menu : Add/Replace                   ##
    ####################################################################

    abc[ "menubar_tops__add_replace"  ] = Menu( abc[ "menubar_tops" ] , tearoff = 1 )

    abc[ "menubar_tops" ].add_cascade( font = "TkFixedFont" , label = "Add/Replace" , menu = abc[ "menubar_tops__add_replace" ] )

    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Escape Characters in (A)'                           , command = lambda: abc__tops__add_replace( "A" , "A" , "\n" , "escape"  ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Add quotes to strings in (A)'                       , command = lambda: abc__tops__add_replace( "A" , "A" , "\n" , "quotes_strings"  ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Add quotes to everything in (A)'                    , command = lambda: abc__tops__add_replace( "A" , "A" , "\n" , "quotes"  ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Pipe (A) with a Newline (C)'                , command = lambda: abc__tops__add_replace( "A" , "C" , "|"  , "\n"      ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace single space (A) with a Newline (C)'        , command = lambda: abc__tops__add_replace( "A" , "C" , " "  , "\n"      ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Comma (A) with a Newline (C)'               , command = lambda: abc__tops__add_replace( "A" , "C" , ","  , "\n"      ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace tab (A) with a Newline (C)'                 , command = lambda: abc__tops__add_replace( "A" , "C" , "\t" , "\n"      ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with a Pipe (C)'                , command = lambda: abc__tops__add_replace( "A" , "C" , "\n" , "|"       ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with a comma (C)'               , command = lambda: abc__tops__add_replace( "A" , "C" , "\n" , ","       ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with a tab (C)'                 , command = lambda: abc__tops__add_replace( "A" , "C" , "\n" , "\t"      ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with space (C)'                 , command = lambda: abc__tops__add_replace( "A" , "C" , "\n" , " "       ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with double space (C)'          , command = lambda: abc__tops__add_replace( "A" , "C" , "\n" , "\n\n"    ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with nothing (C)'               , command = lambda: abc__tops__add_replace( "A" , "C" , "\n" , ""        ) )
    abc[ "menubar_tops__add_replace"      ].add_command( font = "TkFixedFont" , label = 'Replace Newline (A) with OR (C)'                    , command = lambda: abc__tops__add_replace( "A" , "C" , "\n" , " OR "    ) )

    ####################################################################
    ##                Text Ops Menu : String Reversals                ##
    ####################################################################


    ####################################################################
    ##                    Text Ops Menu : Examples                    ##
    ####################################################################

    ####################################################################

    abc[ "menubar_tops" ].add_separator()

    ####################################################################

    abc[ "menubar_tops__examples" ] = Menu( abc[ "menubar_tops" ] , tearoff = 1 )

    abc[ "menubar_tops" ].add_cascade( font = "TkFixedFont" , label = "Text Ops Examples" , menu = abc[ "menubar_tops__examples" ] )

    abc[ "menubar_tops__examples" ].add_command( font = "TkFixedFont" , label = 'String Interpolate : Ping'            , command = lambda: abc__tops__examples( "abc__tops__interpolate_ping" ) )
    abc[ "menubar_tops__examples" ].add_command( font = "TkFixedFont" , label = 'String Interpolate : Ping with status', command = lambda: abc__tops__examples( "abc__tops__interpolate_ping_status" ) )
    abc[ "menubar_tops__examples" ].add_command( font = "TkFixedFont" , label = 'String Interpolate : Ping with color' , command = lambda: abc__tops__examples( "abc__tops__interpolate_ping_color" ) )
    abc[ "menubar_tops__examples" ].add_command( font = "TkFixedFont" , label = 'String Interpolate : NMap Advanced'   , command = lambda: abc__tops__examples( "abc__tops__interpolate_nmap_advanced" ) )


    ####################################################################

    abc[ "menubar_tops" ].add_separator()

    ####################################################################

    abc[ "menubar_tops__help" ] = Menu( abc[ "menubar_tops" ] , tearoff = 1 )

    abc[ "menubar_tops" ].add_cascade( font = "TkFixedFont" , label = "Help with Text Ops functions" , menu = abc[ "menubar_tops__help" ] )

    abc[ "menubar_tops__help" ].add_command( font = "TkFixedFont" , label = 'Help : sort (A) and unique (C)' , command = lambda: abc__tops__help( "abc__tops__sort_unique" ) )

# endregion  ## Text Ops Menu ##########################################


########################################################################
##                         Text Ops Functions                         ##
########################################################################

# region     # Text Ops Functions ######################################

def abc__tops__examples( help_with ) : 

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


def abc__tops__help( help_with ) : 

    if help_with == "abc__tops__sort_unique" :

        message_text  = "This will sort and deduplicate all lines in Box A and print the results in Box C"

        messagebox.showinfo( 'Text Ops : sort and unique' , message_text )


def abc__tops__randomize_list( fm_box , to_box ) :

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


def abc__tops__split_by_n_lines( fm_box , to_box ) :

    print( f'# INFO # {"abc__tops__split_by_n_lines":48} # fm_box : {fm_box} | to_box : {to_box}')

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

            if i % split_by_int == 0 : box[ to_box ].insert( "end" , abc[ "options_record_separator" ].get() )

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


def abc__tops__add_replace( fm_box , to_box , find_this , repl_with ) :

    print( f'# INFO # {"abc__tops__add_replace":48} # fm_box : {fm_box} | to_box : {to_box} | find_this : {find_this} | repl_with : {repl_with}')

    if   repl_with == "escape" :

        lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

        lst_fm = [ f'{re.escape(x)}' for x in lst_fm if x and x.strip() ]

        _clear_box( to_box )

        for x in lst_fm :

            box[ to_box ].insert( "end" , f'{x}\n' )

    elif repl_with == "quotes" :

        lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

        lst_fm = [ f'"{x}"' for x in lst_fm if x and x.strip() ]

        _clear_box( to_box )

        for x in lst_fm :

            box[ to_box ].insert( "end" , f'{x}\n' )

    elif repl_with == "quotes_strings" :

        # todo floats showing up as strings. isnumeric, isdigit.. not working.
        # figure out something else to avoid quotes around things that do not need quotes

        lst_fm = [ x for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() if x and x.strip() ]

        _clear_box( to_box )

        for x in lst_fm :

            if   isinstance( x , str )   : box[ to_box ].insert( "end" , f'"{x}"\n' )
            elif isinstance( x , int )   : box[ to_box ].insert( "end" ,  f'{x}\n'  )
            else                         : box[ to_box ].insert( "end" , f'"{x}"\n' )

    elif find_this == "\n" :

        lst_fm = [ x for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() if x and x.strip() ]

        _clear_box( to_box )

        box[ to_box ].insert( "end" , f'{repl_with.join(lst_fm)}\n' )

    else :

        lst_fm = box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines()

        lst_fm = [ x for x in lst_fm if x and x.strip() ]

        _clear_box( to_box )

        for x in lst_fm :

            for y in x.split( find_this ) :

                box[ to_box ].insert( "end" , f'{y}\n' )


def abc__tops__multiple_grep() : pass


def abc__tops__bulk_replace() : pass


def abc__tops__string_interpolate( vars_box , str_box , to_box ) :

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

# endregion  # Text Ops Functions ######################################














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

def menubar_code() :

    abc[ "menubar_code"     ] = Menu( abc[ "menubar" ] , tearoff = 1 ) ; abc[ "menubar" ].add_cascade( label = "Code" , menu = abc[ "menubar_code" ] )

    ####################################################################
    ##                         Code Comments                          ## Something here looks familiar
    ####################################################################

    abc[ "menubar_code__cmnt"     ] = Menu( abc[ "menubar_code" ] , tearoff = 1 )

    abc[ "menubar_code"  ].add_cascade( font = "TkFixedFont" , label = "Code Comments" , menu = abc[ "menubar_code__cmnt"     ] )

    abc[ "menubar_code"             ].add_command( font = "TkFixedFont" , label = 'Build Python List (C) from lines in (A)'                                            , command = lambda: abc__code__build_structures( **{ "fm_box":"A" , "to_box":"C" , "do_this":"py_list"                       } ) )
    abc[ "menubar_code"             ].add_command( font = "TkFixedFont" , label = 'Build Python List (C) from lines in (A) with newline'                               , command = lambda: abc__code__build_structures( **{ "fm_box":"A" , "to_box":"C" , "do_this":"py_list" , "delim" : "newline" } ) )

    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 Center Space Pad with VS Code Folding'   , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 Center Space Pad with VS Code Folding'   , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 Center Space Pad with VS Code Folding'   , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    #                                                                                                                                                                                                                                                                                                                            #
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    #                                                                                                                                                                                                                                                                                                                            #
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W64 Center Space Pad'                        , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    #                                                                                                                                                                                                                                                                                                                            #
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 Left Pound Pad with VS Code Folding'     , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 Right Pound Pad'                         , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 Right Pound Pad with VS Code Folding'    , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt"       ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 Right Pound Pad with VS Code Folding'    , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )

    ####################################################################

    #abc[ "menubar_code" ].add_separator()

    ####################################################################

    abc[ "menubar_code__cmnt_more" ] = Menu( abc[ "menubar_code__cmnt"    ] , tearoff = 1 )

    abc[ "menubar_code__cmnt"    ].add_cascade( font = "TkFixedFont" , label = "More Code Comments" , menu = abc[ "menubar_code__cmnt_more" ] )

    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I 0 --VL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W":72 , "I": 0 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W72 I 0 --VR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W":72 , "I": 0 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W68 I 4 --VL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W":68 , "I": 4 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H0 W68 I 4 --VR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":0 , "W":68 , "I": 4 , "cmnt_align":"-" , "cmnt_pad":"-" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I 0 CPVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I 0 CPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I 0 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I 0 CSVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I 0 CSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I 0 RPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W48 I 0 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W64 I 8 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W64 I 8 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":64 , "I": 8 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W68 I 4 CPVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W68 I 4 CPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W68 I 4 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W68 I 4 CSVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W68 I 4 CSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W68 I 4 RPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W68 I 4 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I 0 CPVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I 0 CPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I 0 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I 0 CSVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I 0 CSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I 0 RPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H1 W72 I 0 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":1 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I 0 CPVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I 0 CPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I 0 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) , columnbreak = 1 )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I 0 CSVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I 0 CSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I 0 RPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W48 I 0 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W60 I12 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":60 , "I":12 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W64 I 8 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W64 I 8 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":64 , "I": 8 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 I 4 CPVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 I 4 CPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 I 4 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 I 4 CSVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 I 4 CSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 I 4 RPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W68 I 4 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I 0 CPVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I 0 CPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I 0 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I 0 CSVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I 0 CSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I 0 RPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H2 W72 I 0 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":2 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I 0 CP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I 0 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":48 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I 0 LP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":48 , "I": 0 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I 0 LS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":48 , "I": 0 , "cmnt_align":"L" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I 0 RP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W48 I 0 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":48 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W60 I12 CP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":60 , "I":12 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W60 I12 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":60 , "I":12 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W60 I12 LP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":60 , "I":12 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) , columnbreak = 1 )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W60 I12 RP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":60 , "I":12 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W60 I12 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":60 , "I":12 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W64 I 8 CP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W64 I 8 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":64 , "I": 8 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W64 I 8 LP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":64 , "I": 8 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W64 I 8 RP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":64 , "I": 8 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W64 I 8 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":64 , "I": 8 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 CP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 CPVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 CPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 CSVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 CSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 LP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 RP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 RPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W68 I 4 RSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":68 , "I": 4 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 CP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 CPVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 CPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 CS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 CSVL' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"L" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 CSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"C" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 LP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"L" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 RP--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 RPVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"P" , "fold_type":"V" , "fold_align":"R" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 RS--' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"-" , "fold_align":"-" } ) )
    abc[ "menubar_code__cmnt_more"  ].add_command( font = "TkFixedFont" , label = 'String from (A) to Code Comment (C) H3 W72 I 0 RSVR' , command = lambda: abc__code__fancy_comments( **{ "fm_box":"A" , "to_box":"C" , "head":3 , "W":72 , "I": 0 , "cmnt_align":"R" , "cmnt_pad":"S" , "fold_type":"V" , "fold_align":"R" } ) )


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

    #print( '# = '*20 + '#' )
    #for k,v in kwargs.items() : print( f'# {k:>37} : {v:<37} #' )
    #print( '# = '*20 + '#' )

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
         

def abc__code__hash_function( **kwargs ) :  ## eac3d72c85cdbe517a7c32064e722011 # 2024-04-01 00:23:37 #
    
    fm_box  = kwargs.get( "fm_box"  , "C" )
    to_box  = kwargs.get( "to_box"  , fm_box )

    timenow = datetime.datetime.now()

    print( f'# INFO # {timenow:%Y-%m-%d %H:%M:%S} # {getframeinfo(currentframe()).lineno:4,d} # abc__code__hash_function( {{ "fm_box" : "{fm_box}" }} )' )

    lst_orig = [ x.rstrip() for x in box[ fm_box ].get( "1.0" , 'end-1c' ).splitlines() ]

    ## Remove Leading Blank lines 
    while lst_orig[0] == '' : lst_orig.pop(0)

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

def menubar_misc() :

    abc[ "menubar_misc"     ] = Menu( abc[ "menubar" ] , tearoff = 1 ) ; abc[ "menubar" ].add_cascade( label = "Misc"      , menu = abc[ "menubar_misc"     ] )

    ####################################################################
    ##                Misc Menu : Generate Random Data                ##
    ####################################################################

    abc[ "menubar_misc_random"  ] = Menu( abc[ "menubar_misc" ] , tearoff = 1 )

    abc[ "menubar_misc" ].add_cascade( font = "TkFixedFont" , label = "Generate Random Data" , menu = abc[ "menubar_misc_random"  ] )

    abc[ "menubar_misc_random" ].add_command( font = "TkFixedFont" , label = 'X Y Decimal Coordinates (C)'               , command = lambda: abc__misc__gen_random_data( "C" , "xy coords" ) )
    abc[ "menubar_misc_random" ].add_command( font = "TkFixedFont" , label = 'Y X Decimal Coordinates (C)'               , command = lambda: abc__misc__gen_random_data( "C" , "yx coords" ) )
    abc[ "menubar_misc_random" ].add_command( font = "TkFixedFont" , label = 'Epoch dates (C)'                           , command = lambda: abc__misc__gen_random_data( "C" , "epoch"     ) )

    ####################################################################
    ##                Misc Menu : Cryptographic Hashes                ##
    ####################################################################

# endregion  ## Misc Menu ##########################################


########################################################################
##                           Misc Functions                           ##
########################################################################

# region     # Misc Functions ##########################################

def abc__misc__gen_random_data( to_box , do_this ) :

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

# endregion  # Misc Functions ##########################################












########################################################################
#                             Execute Main                             #
########################################################################

# region     # Execute Main ############################################

if __name__ == '__main__' : main()

# endregion  # Execute Main ############################################



