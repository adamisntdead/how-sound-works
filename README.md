# How Sound Works🔊

> An explainer video built with 3blue1brown's [manim](https://github.com/3b1b/manim)

![Watch The Video](https://i.imgur.com/RthFlPS.png)

This is the source code for the animation that Sam Enright and I made for the [ReelLIFE Science](https://reellifescience.com) competition.
It uses the software developed by [3blue1brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw).

## Creating The Animations

https://github.com/3b1b/manim/commit/31478c523c9febb85d673219c6451ce545b5e319

Manim changes quite regularly, so to make the animations, I would reccommend just using the same version that these were created with.
First, you will need to get a local copy of manim.

```bash
$ git clone https://github.com/3b1b/manim
$ cd manim
$ git reset --hard 31478c523c9febb85d673219c6451ce545b5e319
```

Now you can follow the installation instructions in the `manim/README.md` file.
When that is installed and setup, you can run these animations.
Clone down this repo, and copy the scenes folder and build.sh into your manim folder and then you can run `build.sh`.

```bash
$ git clone https://github.com/adamisntdead/how-sound-works
$ cd how-sound-works
$ cp -a scenes PATH_TO_MANIM/scenes
$ cp -a build.sh PATH_TO_MANIM/build.sh
$ cd PATH_TO_MANIM
$ sh build.sh
```

## License 

MIT, Copyright Sam Enright and Adam Kelly.