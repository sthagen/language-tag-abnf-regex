# language-tag-abnf-regex

Test repository for the ABNF translation of language tag codes into a regular expression for CSAF.

Base information from:
```
[BCP47] Phillips, A. and M. Davis, "Matching of Language Tags", BCP 47, RFC 4647, September 2006. 
        Phillips, A., Ed., and M. Davis, Ed., "Tags for Identifying Languages", BCP 47, RFC 5646, September 2009.
        https://www.rfc-editor.org/info/bcp47
```
Direct link: https://www.rfc-editor.org/rfc/bcp/bcp47.txt

## Status

Experimental.

## Transformation

Here is the regex suggested initially for CSAF: 
```
^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-x(-[A-Za-z0-9]{1,8})+)?|x(-[A-Za-z0-9]{1,8})+|i-default|i-mingo)$
```

And the way to it:
```
Language-Tag = langtag | privateuse | grandfathered

langtag = language(-script)?(-region)?(-variant)*(-extension)*(-privateuse)?

language = ([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})
script = [A-Za-z]{4}
region = ([A-Za-z]{2}|[0-9]{3})
variant = ([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3})
extension = [A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+

privateuse = x(-[A-Za-z0-9]{1,8})+
grandfathered = i-default|i-mingo
```

Source: @tschmidtb51 in https://github.com/oasis-tcs/csaf/issues/71

A regex that consumes matches all present test cases derived from ABNF grammar of BCP 47 is:

```
^(([A-Za-z]{2,3}(-[A-Za-z]{3}(-[A-Za-z]{3}){0,2})?|[A-Za-z]{4,8})(-[A-Za-z]{4})?(-([A-Za-z]{2}|[0-9]{3}))?(-([A-Za-z0-9]{5,8}|[0-9][A-Za-z0-9]{3}))*(-[A-WY-Za-wy-z0-9](-[A-Za-z0-9]{2,8})+)*(-[xX](-[A-Za-z0-9]{1,8})+)?|[xX](-[A-Za-z0-9]{1,8})+|[eE][nN]-[gG][bB]-[oO][eE][dD]|[iI]-[aA][mM][iI]|[iI]-[bB][nN][nN]|[iI]-[dD][eE][fF][aA][uU][lL][tT]|[iI]-[eE][nN][oO][cC][hH][iI][aA][nN]|[iI]-[hH][aA][kK]|[iI]-[kK][lL][iI][nN][gG][oO][nN]|[iI]-[lL][uU][xX]|[iI]-[mM][iI][nN][gG][oO]|[iI]-[nN][aA][vV][aA][jJ][oO]|[iI]-[pP][wW][nN]|[iI]-[tT][aA][oO]|[iI]-[tT][aA][yY]|[iI]-[tT][sS][uU]|[sS][gG][nN]-[bB][eE]-[fF][rR]|[sS][gG][nN]-[bB][eE]-[nN][lL]|[sS][gG][nN]-[cC][hH]-[dD][eE])$
```

## Report

The current regular expression candidate passes all 1000 tests from corpus.

### Details

```
collected 1014 items

tests/test_regex.py ................................................................................................................................................................................................................................................... [ 23%]
....................................................................................................................................................................................................................................................................... [ 49%]
....................................................................................................................................................................................................................................................................... [ 75%]
.....................................................................................................................................................................................................................................................                   [100%]

============================================================================================================================ 1014 passed in 2.17s =============================================================================================================================
```

### Other Reports

Using only the first 100 test cases and a different external validator from Christoph Schneegans:

[https://schneegans.de/lv/?tags=X-Z...](https://schneegans.de/lv/?tags=X-Z%0D%0ANhr-826-x-37xd5v10-4-95G-4b0-McE-q-z-649-tJ-3232Sm-C-8%0D%0AI-TAO%0D%0Ax-sK-aT-QU-Xul-j-oif-IF%0D%0AwORgynep-VkYL-3WHP-DBAgB-cargOZkD-6jNC-YGpgM-dAhKA-7EZG-0Rrx-OZMlCbo-2vhf-5wkc-7OFG-wRKmQ-lGajd-3CKC-1Yrl-1FqL-7ztG-1gjk-z-xMFaehZZ%0D%0AEDuiK-naTz-Lo-B-4s-bXQn-351-75-1V-F04V-U2-53n-gw-Ot-c7-egjG-X-1%0D%0ArjuM-Ne-Z-gO-Tl-8-5UyR-x-02O6CWc%0D%0Ags-REm-9F57ro%0D%0AZH-XIANG%0D%0AoUr-7c8D-1t3E08-Y52Cr8-X-z%0D%0AZH-HAKKA%0D%0AZP-yhG-FzX-Znu-pqoK-073-6e82-9r8C-0wI8%0D%0AKXrXG-hQBc%0D%0Ai-tsu%0D%0ACvML-FazM-x-5%0D%0ALBwhXW-dQRH-599-Q-2Q0-x-aN%0D%0AI-PWN%0D%0AsgG-ppEv-0w6s-8Y86-W-4uW-0Cb-x-l%0D%0Atpxe-Ha-c-cY4-x-H-D-O-D-GxN64rG%0D%0AIlDcnl-vDct-Kf%0D%0AlN-BtU-PNV-GiB-8LOv-4I14-x-d-DY2w-R6%0D%0Ajm-VaA-0gEH1%0D%0Ai-ami%0D%0AIrzH-zfOI-103-y-tqnGh0%0D%0AZH-GUOYU%0D%0AztTF-M-G7%0D%0AART-LOJBAN%0D%0AkhzJ-x-5E-5%0D%0Azh-guoyu%0D%0Ano-bok%0D%0Asgn-be-fr%0D%0AoCt-HJe-oGtt-L-30U-F5-7l-Y-bI-C-98-X-7V6W2-ns%0D%0AzIrezey-zAvB-x-7-6%0D%0AWpGTR-Nz-pbign-X-q77%0D%0APTqo-124%0D%0AFkbev-Fbrz-oe-I-Q7-X-b%0D%0ASGN-BE-FR%0D%0AFK-mQu-WJs-crL-X-33-NuH893eK-N-9-6U2%0D%0AZH-MIN-NAN%0D%0AVJCq-mtKh-567p6-3b2r-l-86-x-26%0D%0ACEL-GAULISH%0D%0AIXdQbMDl-jal84-1R37%0D%0Aoxc-GXL-eIt-gsPP-zb-5053-N-23g-X-2%0D%0Azh-min%0D%0AlGnU-449-J0p3i836-6AxS-38Y41mt%0D%0AGGw-85Ee-H-16%0D%0AHqH-gxZU-451-u-wg4-d-5hK0%0D%0Acel-gaulish%0D%0Azh-xiang%0D%0AvBgj-XoTH-sh4ectk%0D%0ASGN-CH-DE%0D%0AZH-MIN%0D%0Ai-hak%0D%0AADTRG-324-Um924-1z85-34421-U-I772287-6a-13-fIwq6-n-rQ7-X-7p-ln44%0D%0AWQSm-MczP-Gg-2952-906p6-S-1Pv-Z9-I9y4-e-0w%0D%0ANO-BOK%0D%0AkA-rPb-npj-TCq-jX%0D%0Azh-min-nan%0D%0ARwdz-ngzf-577-46Jt54m8-22h3-78721-5f16-02zT-R-Pq20k-8l3-013i-0mT5N-eU-P347-m1-o-5a-x-1%0D%0Azh-hakka%0D%0AbwCu-TuLm-X-B-01-0-F-Kf%0D%0Asgn-ch-de%0D%0Aart-lojban%0D%0ATAiCvajp-wtia-101Jo9-6PY33K64-w-16-8wJ8%0D%0AQCnL-MJ-X-I%0D%0APz-yW%0D%0AI-HAK%0D%0ASGN-BE-NL%0D%0AtLCF-Oe-11qy-559c9v-k7nR94Ev-s-6VPx-1M-T-fb-t60K0-c1621X-1637-E-052-69-f4-p0-7qR-x-g%0D%0ATKq-aOFp-59tEt-904c-X-5m-84-ImZ%0D%0AI-MINGO%0D%0ANO-NYN%0D%0AOPLye-PAwd-Se-x-842-2%0D%0AI-TAY%0D%0Ano-nyn%0D%0AYhIlc-ReAB%0D%0Ai-default%0D%0Ai-tay%0D%0AUHV-Iifv-871-0vQ8-1o436TF-8H643-X-4-1U2V-5G-5-W-A2%0D%0AsDLW-Fs-X-ce76-M-N-8em%0D%0AiKy-Nsp-dLrJ-Lz-iylm5-P-Y0-V8%0D%0Ai-mingo%0D%0AI-NAVAJO%0D%0ABuXFIG-isvR-h-00-x-28-7%0D%0AI-TSU%0D%0AYF-bEC-XJV-Szsq-NZ-p-70-A-3B%0D%0AI-KLINGON%0D%0AAJ-yhH-eY%0D%0ATbuzXlz-fa-f-0S-U6-BI%0D%0Ai-pwn%0D%0AJpxKkOc-McbZ-141%0D%0AJp-NY%0D%0AEqiRNS-4316-0s57-9Ufq-X-9-k-w1-9F%0D%0AAIVRNKl-a-0wM17-k8-73%0D%0AI-ENOCHIAN%0D%0ALzx-uzi-AYU%0D%0AI-AMI%0D%0Ai-navajo%0D%0ANaTOKE-20yuw5u4-3HMh-Q0b6zT-V-xT6qg-XxC9-k-Q85-g-38-K-Y36m3-16JD-5k13R-M4zh%0D%0Ai-klingon&format=text)

A report of these first 100 test cases in JSON format as generated by schneegans.de validator is temporarily stored [here](report-1-100-schneegans-dot-de-report.json).


**Note**: The default branch is `default`.

