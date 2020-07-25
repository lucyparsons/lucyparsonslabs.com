
## Style Guide

In order to keep the LPL website looking consistent aesthetically, we use the Gem file `pxlsrt` to generate images. However, because command line options are not very well documented, you may have to experiment with various thresholds.

We like both the `smart` and `kim` algorithms for generating images. However the default values need to be overwritten.

## Syntax

The syntax for `pxlsrt` assumes INPUT is a `.png` file. JPG files will not work.

```
pxlsrt algorithm INPUT OUTPUT
```

Below are some sample commands we ran. With Kim you set the thresholds with `-v` but for Smart you use the `-t` flag. In the smart example below, the `-v flag` sorts vertically.

```
pxlsrt kim -v 80 newsroom.png newsroom_kim_80.png
pxlsrt smart -v -t 80 newsroom.png newsroom_uniq_v_80.png
```

## Other Examples

If you choose to experiment further, you can change the method with the -m flag. You can sort pixels based on colors, random values, along different colors etc. `pxlsrt help ALGORITHM` will give you more information.

```
pxlsrt smart -r -s -m hue -t 80 newsroom.png newsroom_smart_r_s_hue_80.png
pxlsrt smart -s -m uniqueness -t 80 newsroom.png newsroom_uniq_r_s_b_80.png
pxlsrt smart -v -m random -t 80 newsroom.png newsroom_rand_v_80.png
```
