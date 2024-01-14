#!/usr/bin/python3
"""
The console, to manage everything
"""
import cmd
import re
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Contains the functionality of the console"""
    prompt = '(hbnb) '
    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
            }

    def do_create(self, line):
        """Creates a new object"""
        if len(line) == 0:
            print("** class name missing **")
        elif line not in self.__class__.classes.keys():
            print("** class doesn't exist **")
        else:
            obj = self.__class__.classes[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """ Prints the string representation of an instance
        Args:
            line -> Class id ( In that order)
        """
        class_object = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif class_object[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(class_object) == 1:
            print("** instance id missing **")
            return
        else:
            key = class_object[0] + "." + class_object[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key]
                print(str(obj))

    def do_update(self, line):
        """Updates attributes of an object"""
        updates = line.split(" ")
        if len(line) == 0:
            print("** class name missing **")
            return
        elif updates[0] not in __class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(updates) == 1:
            print("** instance id missing **")
            return
        elif len(updates) == 2:
            print("** attribute name missing **")
        elif len(updates) == 3:
            print("** value missing **")
        else:
            key = updates[0] + "." + updates[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                obj = all_instances[key]
                setattr(obj, updates[2], updates[3])
                storage.save()

    def do_destroy(self, args):
        """Destroys an object based on the Class Name and ID"""

        target_list = args.split(" ")
        if len(args) == 0:
            print("** class name missing **")
            return
        elif target_list[0] not in self.__class__.classes.keys():
            print("** class doesn't exist **")
            return
        elif len(target_list) == 1:
            print("** instance id missing **")
            return
        else:
            key = target_list[0] + "." + target_list[1]
            all_instances = storage.all()
            if key not in all_instances.keys():
                print("** no instance found **")
            else:
                del all_instances[key]
                storage.save()

    def do_all(self, arg):
        """Print string representation of all instances"""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def emptyline(self):
        """Overwrite default behavior to repeat last cmd"""
        pass

    def default(self, arg):
        """default behavior of cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_operations(self, args):
        """Do operations on objects"""

    def do_EOF(self, arg):
        """ Handles EOF to exit program """
        print()
        return True

    def do_quit(self, args):
        """Quits the interpreter"""
        raise SystemExit

    def do_count(self, arg):
        """Count all instances of a class"""
        to_count = args.split(" ")
        instances = 0
        for obj_ in models.storage.all().values():
            if to_count[0] == type(obj_).__name__:
                instances += 1
        print(instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
