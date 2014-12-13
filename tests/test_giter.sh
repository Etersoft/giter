#!/bin/sh

giter()
{
    echo
    echo "$@: "
    #shift
    ../bin/giter "$@"
}

giter list branches
giter print repo name
giter print girar host
giter list remote
giter print girar repo lyx
