#!/usr/bin/python3
"""
This is the main command Line Interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ This is the command Line Interpreter. """
    prompt = '(hbnb) '

def do_nothing(self, lev):
        """ Does nothing """
        pass

def do_quit(self, lev):
        """ Close program and saves safely data """
        return True

def do_EOF(self, lev):
        """ Close program and saves safely data, when
        user input is CTRL + D
        """
        print("")
        return True

def emptyline(self):
        """ Overrides the empty line method """
        pass

Object_dict_all = {"BaseModel": BaseModel,"User": User,"State": State,"City": City,"Amenity": Amenity,
        "Place": Place,
        "Review": Review
            }

def do_create(self, lev):
        """
        This Function will create a new object instance.
        """
        if not lev:
            print("** This is really missing a class name missing **")
            return
        my_Object_data_list = shlex.split(lev)
        if my_Object_data_list[0] not in HBNBCommand.Object_dict_all.keys():
            print("** The class doesn't  at all **")
            return
        The_new_Object_user = HBNBCommand.Object_dict_all[my_Object_data_list[0]]()
        The_new_Object_user.save()
        print(The_new_Object_user.id)


def default(self, lev):
        """ This function will take care of how the data will be injected into the database. """
        All_data_input = {
            "all": self.do_all,
            "count": self.do_count,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update
        }
        lev = lev.strip()
        The_int_data = lev.split(".")

        if len(The_int_data) != 2:
            cmd.Cmd.default(self, lev)
            return
        All_data_names = The_int_data[0]
        The_intepreter = The_int_data[1].split("(")[0]
        linear = ""
        if ( The_intepreter == "update" and  The_int_data[1].split("(")[1][-2] == "}"):
            injection =  The_int_data[1].split("(")[1].split(",", 1)
            injection [0] = shlex.split(injection[0])[0]
            linear = "".join(injection)[0:-1]
            linear = All_data_names + " " +  linear
            self.do_update2(linear.strip())
            return
        try:
            injection  = The_int_data[1].split("(")[1].split(",")
            for fox in range(len(injection)):
                if (fox != len(injection) - 1):
                     linear =  linear + " " + shlex.split(injection[fox])[0]
                else:
                     linear =  linear + " " + shlex.split(injection[fox][0:-1])[0]
        except IndexError:
             injection  = ""
             linear = ""
        linear = All_data_names +  linear
        if ( The_intepreter  in  All_data_input.keys()):
             All_data_input[ The_intepreter](linear.strip())







   

if __name__ == '__main__':
    HBNBCommand().cmdloop()
