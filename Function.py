{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPaJG4dtwsk+UPehr06/6un",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/waghvaishnav/Data-Structure-Playground/blob/main/Function.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "HkH3TYpDqOau"
      },
      "outputs": [],
      "source": [
        "def hello(s):\n",
        "    print('Hello!'+s)\n",
        "    print('Hello!!!'+s)\n",
        "    print('Hello there.')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "hello(\"a\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IEfKUIlZqm6v",
        "outputId": "d00a042f-6893-4b96-aeb8-16d7149d66dd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Hello!a\n",
            "Hello!!!a\n",
            "Hello there.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def Vaishnav(sur):\n",
        "  print(\"vaishnav  \"+sur)\n"
      ],
      "metadata": {
        "id": "I_dpUL5eq74e"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "Vaishnav(\"wagh\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9lRsb2YdrSGK",
        "outputId": "12489222-88e3-4fe7-929e-a0e99d1d3f04"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "vaishnav  wagh\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# function without parameter.\n",
        "def data():\n",
        "  print(\"vaishnav\")\n",
        "  print(\"wagh\")\n",
        "  print(\"add-pune\")\n",
        "  print(\"qualification-graduate\")\n",
        "  print(\"branch-aiml\")\n",
        "  print(\"course-ds\")\n",
        "  print(\"age-22\")\n",
        "  print(\"roll no-45\")"
      ],
      "metadata": {
        "id": "PPDO-g35rVmO"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Qh-L2Azqxf96",
        "outputId": "cb249e60-38fa-4cb3-f916-e01381ae0142"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "vaishnav\n",
            "wagh\n",
            "add-pune\n",
            "qualification-graduate\n",
            "branch-aiml\n",
            "course-ds\n",
            "age-22\n",
            "roll no-45\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# function with the parameter\n",
        "def data(n,s,r,b,a):\n",
        "  print(\"name \"+s)\n",
        "  print(\"sirname \"+n)\n",
        "  print(\"rollno.\"+r)\n",
        "  print(\"branch\"+b)\n",
        "  print(\"age\"+a)"
      ],
      "metadata": {
        "id": "yo3SxIi9xfyQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data(\"vaishnav\",)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xs4rkv8ExfmW",
        "outputId": "57464e24-3345-4c5d-c2ec-4f7857a7810a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "name wagh\n",
            "sirname vaishnav\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def data(s,n):\n",
        "  print(\"name \"+s)\n",
        "  print(\"name \"+n)"
      ],
      "metadata": {
        "id": "JpMQJOtTxfgG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "data(\"hgdh\",\"tfhg\")\n",
        "data(\"efhuhf\",\"hgjghj\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5KwdGYvxxfaQ",
        "outputId": "1792c071-af05-4e5a-a418-64ea7bdb3b00"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "name hgdh\n",
            "name tfhg\n",
            "name efhuhf\n",
            "name hgjghj\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def val_pp(val):\n",
        "    return val, 'as' , val+2\n",
        "\n",
        "r, i, c = val_pp(10)\n",
        "print(r, i, c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "l5M1YGrwxfSd",
        "outputId": "5b1f36d5-bb6f-47a2-ae83-bd2686bcc4ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "10 as 12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def val_pp(val):\n",
        "    return val, val+1 , val+2\n",
        "\n",
        "r, i, c = val_pp(3)\n",
        "print(r, i, c)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "YulgkOpWxfHV",
        "outputId": "36f3987a-a9a9-4c87-8022-e143f8c5c9f8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3 4 5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def value(val):\n",
        "  return val,val+2,val+3\n",
        "\n",
        "r,i,j=value(9)\n",
        "print(r,i,j)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ONkDro6z4APA",
        "outputId": "2bc81fec-d5e3-4023-9a70-9aa32a122bfd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "9 11 12\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def fibonacci(N, a=0, b=1):\n",
        "    counter = 0\n",
        "    while counter < N:\n",
        "        a, b = b, a + b\n",
        "        print(a, end=' ')\n",
        "        counter = counter+1"
      ],
      "metadata": {
        "id": "zpUWzODV5nnI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "fibonacci(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KoI2HGn57MtN",
        "outputId": "a3ae66ca-d418-400f-d445-282188531d3e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1 1 2 3 5 "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def addition(n,a=2):\n",
        "  sum=n+a\n",
        "  print(sum)\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "OiqXEgI25njs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "addition(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bik_UZqT5ng3",
        "outputId": "2b5b9417-5b9e-4db3-8277-6250b3a90205"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "7\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def stu(name,standard=\"btech\",uni=\"pune\"):\n",
        "       print(name,standard,uni)\n",
        "       print(name,standard)\n"
      ],
      "metadata": {
        "id": "LGnVkY3n5nUx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "stu(\"vaishnav\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7gbx9kEc5nJ-",
        "outputId": "40beee8e-ad0f-4bce-d8c9-02e9bc32e0cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "vaishnav btech pune\n",
            "vaishnav btech\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "stu(\"vaishnav\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Uqm1s5l15m9Z",
        "outputId": "ae317464-3543-403a-aa3e-57361493ab97"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "vaishnav btech pune\n",
            "vaishnav btech\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import random\n",
        "\n",
        "def getAnswer(answerNumber):\n",
        "    if answerNumber == 1:\n",
        "        return 'It is certain'\n",
        "    elif answerNumber == 2:\n",
        "        return 'It is decidedly so'\n",
        "    elif answerNumber == 3:\n",
        "        return 'Yes'\n",
        "    elif answerNumber == 4:\n",
        "        return 'Reply hazy try again'\n",
        "    elif answerNumber == 5:\n",
        "        return 'Ask again later'\n",
        "    elif answerNumber == 6:\n",
        "        return 'Concentrate and ask again'\n",
        "    elif answerNumber == 7:\n",
        "        return 'My reply is no'\n",
        "    elif answerNumber == 8:\n",
        "        return 'Outlook not so good'\n",
        "    elif answerNumber == 9:\n",
        "        return 'Very doubtful'"
      ],
      "metadata": {
        "id": "bRh_H_Oz82B0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "fortune = getAnswer(4)\n",
        "print(fortune)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "A_x2DiFv82Ef",
        "outputId": "20a4b30f-fb7d-4eaf-8691-56455eb2ff8c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Reply hazy try again\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# None == var\n",
        "var=10"
      ],
      "metadata": {
        "id": "GZBaODgC82G5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a function to calculate the cube of a number that is passed as the argument to the function.\n",
        "def cube(number):\n",
        "  print(number**3)"
      ],
      "metadata": {
        "id": "fmy6IBAX82JJ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cube(3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "m0k9WZ8E82LE",
        "outputId": "e14825e1-6963-4460-81ae-1685b59649bb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "27\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def cube(number):\n",
        "  return number**3"
      ],
      "metadata": {
        "id": "bYgZYuuZ82Op"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cube(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "qVEJXPivBWSk",
        "outputId": "f2817534-d77c-43f1-cb67-b71d1f8dac61"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "125"
            ]
          },
          "metadata": {},
          "execution_count": 82
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a function to calculate the sum of square of 2 numbers that are defined as the default arguments and its square output is 5."
      ],
      "metadata": {
        "id": "j7ZOG1E4BWPA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def sum(a=2,b=1):\n",
        "  print(b+a**2)"
      ],
      "metadata": {
        "id": "Lb3B_unpBV5V"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sum()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "IGvbNHT_CMc4",
        "outputId": "1d7e90af-ac6f-4043-f33b-9a620c91a282"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def cal_fact(number):\n",
        "  out=1\n",
        "  for i in range(1,number):\n",
        "    out=out*i\n",
        "\n",
        "\n",
        "  return(out)\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "dNiHeFysCMZh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "cal_fact(4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SbwLs-EaCMWm",
        "outputId": "779fd2f9-c8c5-4695-acae-a8dd4f83c377"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "362880\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Correct the syntax of the following function to get the required output.\n",
        "\n",
        "# Note : Make use of all the concepts covered until now.\n",
        "\n",
        "# Example :\n",
        "\n",
        "def string_concatenation(s2,s1 = 'ai',s3 = 3):\n",
        "\n",
        "    if s3 == 3:\n",
        "      s = (s1 + s2) * s3\n",
        "      print(s,end = \"\")\n",
        "    else:\n",
        "      s = s1 + s2 * 1\n",
        "      print(s,end = '')\n",
        "\n",
        "    # string_concatenation('adventures')\n",
        "\n",
        "#     >>> 'aiadventuresaiadventuresaiadventures'"
      ],
      "metadata": {
        "id": "E1UmVUKiCMMS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "string_concatenation(s2=\"adventures\",s1=\"ai\",s3=3)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Js57Q-bSCMCu",
        "outputId": "38965abf-374c-48c6-d03a-2b5954e030f1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "aiadventuresaiadventuresaiadventures"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "string_concatenation('vaish', 'nav', 4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mNvggLCmI2Eb",
        "outputId": "6c7131da-2a0c-4640-9d3b-aac1106de578"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "navvaish"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a function to calculate the area of triangle or rectangle using 3 arguments : base, height and shape.\n",
        "def Area(base,height,shape):\n",
        "  if shape == \"triangle\":\n",
        "    area=(1/2*(base*height))\n",
        "    print(area)\n",
        "  elif shape == \"rectangle\":\n",
        "    area=(base*height)\n",
        "    print(area)\n",
        "\n",
        "\n",
        "Area(5,6,\"triangle\")\n",
        "Area(5,6,\"rectangle\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OrClgSZEKjHH",
        "outputId": "87d635fc-a462-4a26-c128-198045f9e530"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15.0\n",
            "30\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Create a function to calculate and display the sum of the following sequence by taking input from user for n.Sequence : 1 + 1/1! + 1/2! + 1/3! + + 1/n!\n",
        "def sequence():\n",
        "  num=int(input())\n",
        "  sum_fact=1\n",
        "  j=1\n",
        "  while j <= num:\n",
        "    sum_fact=(sum_fact + 1/cal_fact(i))\n",
        "    j=j+1\n",
        "  print(sum_fact)\n"
      ],
      "metadata": {
        "id": "x5ssZ0bFKjDv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# cal_fact(5)\n",
        "sequence()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "j5AWDS2iKjBI",
        "outputId": "45070397-7e9f-4f7a-adbe-fe212c4957ff"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "3\n",
            "1.0000008267195768\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def a():\n",
        "  a = 3\n",
        "  print(\"helllo\")\n",
        "x = a()\n",
        "print(x)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wkkgZM5sKi6U",
        "outputId": "f4b0dd39-cd88-473e-afde-17e858755148"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "helllo\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def a():\n",
        "  return(\"helllo\")\n",
        "x = a()\n",
        "print(x +'!!!')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FOGhQ97QKi20",
        "outputId": "8379a3e4-a6ff-40c2-8232-8eab62d4da2c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "helllo!!!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def ispangram(CHAR):\n",
        "  count=0\n",
        "  str=\"abcdefghijklmnopqrstuvwxyz\"\n",
        "  for i in str:\n",
        "    if i in CHAR:\n",
        "      count+=1\n",
        "  print(count)\n",
        "  if count == 26:\n",
        "    print(\"pangram\")\n",
        "  else:\n",
        "    print(\"not a pangram.\")\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "Jef62wnWKi0A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ispangram(\"a quick brown fox jumps over the lazy dog\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "t_cPMJh9Kit7",
        "outputId": "3450cc56-f70d-4795-9684-6a3693b2c224"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "26\n",
            "pangram\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "C9jSxg8xbVAI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def h():\n",
        "  print(\"python\")\n",
        "x=h()\n",
        "print(h())"
      ],
      "metadata": {
        "id": "YgkYpjK-Rbru",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0b9b27c4-0f14-4589-a13d-5a7b4686bc63"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "python\n",
            "python\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "bo7zjPd9SJHP",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 164
        },
        "outputId": "743737f1-fd13-41a4-f5ae-ed8e544e4355"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "name 'a' is not defined",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-14-fcd8113a4a46>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mx\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0ma\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mNameError\u001b[0m: name 'a' is not defined"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#  Sum of Natural Numbers Write a Python program that calculates the sum of natural numbers from 1 to N.\n",
        "N=int(input(\"enter the vallue of the num.\"))\n",
        "sum=0\n",
        "i=1\n",
        "while i <= N:\n",
        "  sum=sum+i\n",
        "\n",
        "print(sum)\n",
        "i=i+1"
      ],
      "metadata": {
        "id": "UaOLxXu5ZvOt",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 219
        },
        "outputId": "a77c9f3f-8788-4f34-f7f5-16180badf7c5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-12-4eaf034ec832>\u001b[0m in \u001b[0;36m<cell line: 5>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0msum\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m0\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mi\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m \u001b[0;32mwhile\u001b[0m \u001b[0mi\u001b[0m \u001b[0;34m<=\u001b[0m \u001b[0mN\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m   \u001b[0msum\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0msum\u001b[0m\u001b[0;34m+\u001b[0m\u001b[0mi\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: "
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def sum(NUM):\n",
        "\n",
        "   num=int(NUM)\n",
        "   sum=0\n",
        "   for i in range(1,num+1):\n",
        "      sum=sum+i\n",
        "\n",
        "   print(sum)\n",
        "\n"
      ],
      "metadata": {
        "id": "gGekBlpNU0YS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sum(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Z1ddOGEWb8Wf",
        "outputId": "405b3782-4549-4618-86f7-c5415ad1f30a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "15\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "oAaa1Q1IhGP5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "KY2BeyFrhGGB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "Rgp07io6hF2H"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}