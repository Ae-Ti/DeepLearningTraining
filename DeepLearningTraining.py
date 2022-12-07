{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNo/vddpyGOMSuDEGKEileD",
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
        "<a href=\"https://colab.research.google.com/github/Ae-Ti/DeepLearningTraining/blob/main/DeepLearningTraining.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "import matplotlib.pyplot as plt"
      ],
      "metadata": {
        "id": "Lvqe7AH51W7d"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# ordinary least squares, **OLS**"
      ],
      "metadata": {
        "id": "m5DQY_-8ux6B"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "5KnHeYWcJOVm",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 338
        },
        "outputId": "45e1de0c-8b68-4e5c-c100-8ed1cfe550c6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "5.0 90.5\n",
            "20.0 46.0\n",
            "a= 2.3\n",
            "b= 79.0\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        }
      ],
      "source": [
        "x = np.array([2,4,6,8])\n",
        "y = np.array([81,93,91,97])\n",
        "\n",
        "mx = np.mean(x)\n",
        "my = np.mean(y)\n",
        "print(mx,my)\n",
        "\n",
        "divisor=sum([(i-mx)**2 for i in x])\n",
        "def top(x,mx,y,my):\n",
        "  d = 0\n",
        "  for i in range(len(x)):\n",
        "    d+= (x[i]-mx)*(y[i]-my)\n",
        "  return d\n",
        "dividend = top(x,mx,y,my)\n",
        "\n",
        "print(divisor,dividend)\n",
        "a=dividend/divisor\n",
        "b = my-(mx*a)\n",
        "print(\"a=\",a)\n",
        "print(\"b=\",b)\n",
        "\n",
        "plt.plot(x,y,'o')\n",
        "plt.plot(x,(a*x+b))\n",
        "plt.show()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#mean square error, **MSE**"
      ],
      "metadata": {
        "id": "jqFZoVCR07Ze"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "fake_a = 3\n",
        "fake_b = 76\n",
        "\n",
        "x = np.array([2,4,6,8])\n",
        "y = np.array([81,93,91,97])\n",
        "\n",
        "def predict(x):\n",
        "  return fake_a *x +fake_b\n",
        "\n",
        "predict_result = []\n",
        "for i in range(len(x)):\n",
        "  predict_result.append(predict(x[i]))\n",
        "  print(\"x=%.f, real=%.f, prediction=%.f\" %(x[i],y[i],predict(x[i])))\n",
        "\n",
        "n = len(x)\n",
        "def mse(y,y_pred):\n",
        "  return (1/n) * sum((y-y_pred)**2)\n",
        "\n",
        "print(\"mse: \"+str(mse(y,predict_result)))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yIWTiVJA06ya",
        "outputId": "7d944fa2-ed48-44c3-c6ab-9890760876e6"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "x=2, real=81, prediction=82\n",
            "x=4, real=93, prediction=88\n",
            "x=6, real=91, prediction=94\n",
            "x=8, real=97, prediction=100\n",
            "mse: 11.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Gradient Decent** and **Multiple Linear Regression**"
      ],
      "metadata": {
        "id": "8n_zwIGh4nXa"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x1 = np.array([2,4,6,8])\n",
        "x2 = np.array([0,4,2,3])\n",
        "y = np.array([81,93,91,97])\n",
        "\n",
        "fig = plt.figure()\n",
        "ax = fig.add_subplot(111,projection=\"3d\")\n",
        "ax.scatter3D(x1,x2,y)\n",
        "plt.show()\n",
        "\n",
        "a1=0\n",
        "a2=0\n",
        "b=0\n",
        "\n",
        "lr=0.01\n",
        "epochs=2000\n",
        "n= len(x1)\n",
        "\n",
        "for i in range(epochs):\n",
        "  y_pred = a1*x1+a2*x2+b\n",
        "  error = y-y_pred\n",
        "\n",
        "  a1_diff = (2/n)*sum(-x1*(error))\n",
        "  a2_diff = (2/n)*sum(-x2*(error))\n",
        "  b_diff = (2/n)*sum(-(error))\n",
        "\n",
        "  a1 -= lr*a1_diff\n",
        "  a2 -= lr*a2_diff\n",
        "  b -= lr*b_diff\n",
        "\n",
        "  if i%100==0:\n",
        "    print(\"epoch=%.f,a1=%.04f,a2=%.04f,b=%.04f\" % (i,a1,a2,b))\n",
        "\n",
        "print(\"real: \",y)\n",
        "print(\"prediction: \",y_pred)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 652
        },
        "id": "hPCaiTXA3hA-",
        "outputId": "efa93f4c-f600-4fff-cff0-8f24371901ba"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 432x288 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {
            "needs_background": "light"
          }
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "epoch=0,a1=9.2800,a2=4.2250,b=1.8100\n",
            "epoch=100,a1=9.5110,a2=5.0270,b=22.9205\n",
            "epoch=200,a1=7.3238,a2=4.2950,b=37.8751\n",
            "epoch=300,a1=5.7381,a2=3.7489,b=48.7589\n",
            "epoch=400,a1=4.5844,a2=3.3507,b=56.6800\n",
            "epoch=500,a1=3.7447,a2=3.0608,b=62.4448\n",
            "epoch=600,a1=3.1337,a2=2.8498,b=66.6404\n",
            "epoch=700,a1=2.6890,a2=2.6962,b=69.6938\n",
            "epoch=800,a1=2.3653,a2=2.5845,b=71.9160\n",
            "epoch=900,a1=2.1297,a2=2.5032,b=73.5333\n",
            "epoch=1000,a1=1.9583,a2=2.4440,b=74.7103\n",
            "epoch=1100,a1=1.8336,a2=2.4009,b=75.5670\n",
            "epoch=1200,a1=1.7428,a2=2.3695,b=76.1904\n",
            "epoch=1300,a1=1.6767,a2=2.3467,b=76.6441\n",
            "epoch=1400,a1=1.6286,a2=2.3301,b=76.9743\n",
            "epoch=1500,a1=1.5936,a2=2.3180,b=77.2146\n",
            "epoch=1600,a1=1.5681,a2=2.3092,b=77.3895\n",
            "epoch=1700,a1=1.5496,a2=2.3028,b=77.5168\n",
            "epoch=1800,a1=1.5361,a2=2.2982,b=77.6095\n",
            "epoch=1900,a1=1.5263,a2=2.2948,b=77.6769\n",
            "real:  [81 93 91 97]\n",
            "prediction:  [80.76357962 92.97144864 91.42519805 96.75600726]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Multilayer Perceptron**"
      ],
      "metadata": {
        "id": "6NLkPYHy-cb_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "w11 = np.array([-2,-2])\n",
        "w12 = np.array([2,2])\n",
        "w2 = np.array([1,1])\n",
        "b1=3\n",
        "b2=-1\n",
        "b3=-1\n",
        "\n",
        "def MLP(x,w,b):\n",
        "  y = np.sum(w*x)+b\n",
        "  if y<=0:\n",
        "    return 0\n",
        "  else:\n",
        "    return 1\n",
        "\n",
        "def NAND(x1,x2):\n",
        "  return MLP(np.array([x1,x2]),w11,b1)\n",
        "\n",
        "def OR(x1,x2):\n",
        "  return MLP(np.array([x1,x2]),w12,b2)\n",
        "\n",
        "def AND(x1,x2):\n",
        "  return MLP(np.array([x1,x2]),w2,b3)\n",
        "\n",
        "def XOR(x1,x2):\n",
        "  return AND(NAND(x1,x2),OR(x1,x2))\n",
        "\n",
        "for x in [(0,0),(1,0),(0,1),(1,1)]:\n",
        "  y = XOR(x[0],x[1])\n",
        "  print(\"input: \"+str(x)+\" output: \"+str(y))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kBIqSIQyAs4O",
        "outputId": "f304bac4-270d-466b-bdec-bec10122e1b5"
      },
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "input: (0, 0) output: 0\n",
            "input: (1, 0) output: 1\n",
            "input: (0, 1) output: 1\n",
            "input: (1, 1) output: 0\n"
          ]
        }
      ]
    }
  ]
}