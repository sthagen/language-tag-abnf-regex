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

Here is the regex: 
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

## Report

The current regular expression candidate fails 189/1000 tests from corpus.

### Details

```
NO_MATCH (I-TAO) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-3.txt)
NO_MATCH (i-tsu) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-14.txt)
NO_MATCH (I-PWN) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-17.txt)
NO_MATCH (i-ami) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-23.txt)
NO_MATCH (sgn-be-fr) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-31.txt)
NO_MATCH (SGN-BE-FR) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-37.txt)
NO_MATCH (SGN-CH-DE) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-51.txt)
NO_MATCH (i-hak) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-53.txt)
NO_MATCH (sgn-ch-de) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-62.txt)
NO_MATCH (I-HAK) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-67.txt)
NO_MATCH (SGN-BE-NL) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-68.txt)
NO_MATCH (I-MINGO) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-71.txt)
NO_MATCH (I-TAY) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-74.txt)
NO_MATCH (i-tay) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-78.txt)
NO_MATCH (I-NAVAJO) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-83.txt)
NO_MATCH (I-TSU) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-85.txt)
NO_MATCH (I-KLINGON) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-87.txt)
NO_MATCH (i-pwn) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-90.txt)
NO_MATCH (I-ENOCHIAN) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-95.txt)
NO_MATCH (I-AMI) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-97.txt)
NO_MATCH (i-navajo) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-98.txt)
NO_MATCH (i-klingon) <- (tests/abnfgen/language-tag-n-100-s-42/language-tag-100.txt)
NO_MATCH (I-LUX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-101.txt)
NO_MATCH (i-enochian) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-103.txt)
NO_MATCH (i-lux) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-104.txt)
NO_MATCH (i-tao) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-108.txt)
NO_MATCH (i-bnn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-110.txt)
NO_MATCH (I-BNN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-114.txt)
NO_MATCH (I-DEFAULT) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-118.txt)
NO_MATCH (sgn-be-nl) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-123.txt)
NO_MATCH (EN-GB-OED) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-125.txt)
NO_MATCH (en-gb-oed) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-126.txt)
NO_MATCH (I-ami) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-133.txt)
NO_MATCH (i-tAO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-134.txt)
NO_MATCH (i-BNn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-138.txt)
NO_MATCH (I-mIngo) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-141.txt)
NO_MATCH (i-LuX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-147.txt)
NO_MATCH (I-TaY) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-149.txt)
NO_MATCH (SGn-Be-FR) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-163.txt)
NO_MATCH (I-haK) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-165.txt)
NO_MATCH (SGn-BE-fr) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-166.txt)
NO_MATCH (i-mINGO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-171.txt)
NO_MATCH (I-nAvAJO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-172.txt)
NO_MATCH (EN-GB-oED) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-182.txt)
NO_MATCH (i-mINgO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-183.txt)
NO_MATCH (sGn-bE-Nl) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-184.txt)
NO_MATCH (i-aMI) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-197.txt)
NO_MATCH (I-EnOchIan) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-198.txt)
NO_MATCH (I-DeFAUlT) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-210.txt)
NO_MATCH (sgn-be-nL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-217.txt)
NO_MATCH (sgn-BE-fr) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-220.txt)
NO_MATCH (I-Pwn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-233.txt)
NO_MATCH (I-tay) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-246.txt)
NO_MATCH (i-pWN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-249.txt)
NO_MATCH (SGn-Be-fR) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-255.txt)
NO_MATCH (I-DEFAUlT) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-256.txt)
NO_MATCH (i-pwN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-258.txt)
NO_MATCH (en-Gb-OeD) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-259.txt)
NO_MATCH (EN-gB-oeD) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-261.txt)
NO_MATCH (i-tsu) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-272.txt)
NO_MATCH (sgN-BE-FR) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-275.txt)
NO_MATCH (i-tAO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-278.txt)
NO_MATCH (i-lUx) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-279.txt)
NO_MATCH (I-bnN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-283.txt)
NO_MATCH (i-HAk) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-292.txt)
NO_MATCH (i-PWn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-294.txt)
NO_MATCH (EN-Gb-oEd) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-296.txt)
NO_MATCH (I-PWN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-302.txt)
NO_MATCH (I-Ami) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-329.txt)
NO_MATCH (I-MInGO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-343.txt)
NO_MATCH (I-luX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-351.txt)
NO_MATCH (i-tAY) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-352.txt)
NO_MATCH (I-klINGOn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-359.txt)
NO_MATCH (I-eNOcHIAN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-367.txt)
NO_MATCH (I-Tay) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-371.txt)
NO_MATCH (i-eNoChIAn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-375.txt)
NO_MATCH (sgN-CH-de) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-384.txt)
NO_MATCH (sgn-Be-fr) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-388.txt)
NO_MATCH (I-EnoChIaN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-391.txt)
NO_MATCH (sGn-Be-nL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-393.txt)
NO_MATCH (i-AMi) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-394.txt)
NO_MATCH (I-enOChIAn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-396.txt)
NO_MATCH (i-pWN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-397.txt)
NO_MATCH (sgN-be-NL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-400.txt)
NO_MATCH (i-DefAuLt) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-416.txt)
NO_MATCH (i-hak) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-418.txt)
NO_MATCH (i-tAo) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-420.txt)
NO_MATCH (I-dEfauLT) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-421.txt)
NO_MATCH (En-gB-oed) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-422.txt)
NO_MATCH (en-gb-oED) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-426.txt)
NO_MATCH (I-miNgo) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-433.txt)
NO_MATCH (SGN-bE-Nl) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-434.txt)
NO_MATCH (i-naVAJO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-437.txt)
NO_MATCH (I-eNOcHiAN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-441.txt)
NO_MATCH (i-taY) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-442.txt)
NO_MATCH (i-eNoChIan) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-448.txt)
NO_MATCH (i-KLInGON) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-452.txt)
NO_MATCH (i-AMi) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-454.txt)
NO_MATCH (I-Lux) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-461.txt)
NO_MATCH (sgn-Be-NL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-465.txt)
NO_MATCH (SgN-BE-Fr) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-473.txt)
NO_MATCH (I-tAy) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-480.txt)
NO_MATCH (i-aMi) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-482.txt)
NO_MATCH (i-LUX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-484.txt)
NO_MATCH (I-luX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-485.txt)
NO_MATCH (I-tAo) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-487.txt)
NO_MATCH (I-PWN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-488.txt)
NO_MATCH (I-PWN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-503.txt)
NO_MATCH (I-TAY) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-504.txt)
NO_MATCH (I-aMi) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-505.txt)
NO_MATCH (sgn-Ch-dE) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-514.txt)
NO_MATCH (SGn-Be-fR) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-519.txt)
NO_MATCH (I-DeFAULt) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-523.txt)
NO_MATCH (I-tao) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-532.txt)
NO_MATCH (I-kLingoN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-541.txt)
NO_MATCH (i-bnn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-542.txt)
NO_MATCH (I-amI) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-565.txt)
NO_MATCH (I-HAK) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-571.txt)
NO_MATCH (i-AmI) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-585.txt)
NO_MATCH (I-PwN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-602.txt)
NO_MATCH (sGN-ch-de) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-606.txt)
NO_MATCH (I-MIngo) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-607.txt)
NO_MATCH (i-HAK) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-613.txt)
NO_MATCH (i-luX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-628.txt)
NO_MATCH (i-luX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-639.txt)
NO_MATCH (i-MiNGo) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-643.txt)
NO_MATCH (I-KlingoN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-650.txt)
NO_MATCH (sgN-Be-NL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-659.txt)
NO_MATCH (I-MingO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-662.txt)
NO_MATCH (i-aMi) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-664.txt)
NO_MATCH (i-lUX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-668.txt)
NO_MATCH (SGN-Be-NL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-671.txt)
NO_MATCH (i-AmI) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-672.txt)
NO_MATCH (sGN-be-FR) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-677.txt)
NO_MATCH (I-tSU) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-680.txt)
NO_MATCH (i-kLInGon) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-687.txt)
NO_MATCH (i-pWn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-716.txt)
NO_MATCH (Sgn-cH-DE) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-724.txt)
NO_MATCH (i-Tay) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-730.txt)
NO_MATCH (sGN-Be-NL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-731.txt)
NO_MATCH (I-enoChiAn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-741.txt)
NO_MATCH (i-tsu) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-753.txt)
NO_MATCH (I-nAVAJO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-756.txt)
NO_MATCH (I-KLINGon) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-758.txt)
NO_MATCH (I-TAy) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-759.txt)
NO_MATCH (I-bNN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-776.txt)
NO_MATCH (i-miNGO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-791.txt)
NO_MATCH (I-NAvAJo) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-792.txt)
NO_MATCH (I-KLInGon) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-801.txt)
NO_MATCH (i-Bnn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-805.txt)
NO_MATCH (i-tsU) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-807.txt)
NO_MATCH (I-tAy) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-809.txt)
NO_MATCH (i-BNn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-815.txt)
NO_MATCH (i-BNN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-817.txt)
NO_MATCH (sGn-bE-nL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-818.txt)
NO_MATCH (I-TAO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-819.txt)
NO_MATCH (Sgn-CH-De) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-825.txt)
NO_MATCH (i-lux) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-832.txt)
NO_MATCH (i-PWN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-837.txt)
NO_MATCH (i-lux) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-839.txt)
NO_MATCH (en-Gb-OEd) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-842.txt)
NO_MATCH (i-PWn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-848.txt)
NO_MATCH (i-AmI) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-849.txt)
NO_MATCH (Sgn-BE-fR) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-858.txt)
NO_MATCH (i-BNn) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-860.txt)
NO_MATCH (sGN-BE-NL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-862.txt)
NO_MATCH (I-mIngO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-864.txt)
NO_MATCH (sgn-be-NL) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-867.txt)
NO_MATCH (I-aMi) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-873.txt)
NO_MATCH (i-LuX) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-875.txt)
NO_MATCH (i-Ami) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-878.txt)
NO_MATCH (i-kLINgON) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-885.txt)
NO_MATCH (i-KlINGon) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-886.txt)
NO_MATCH (sgn-cH-de) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-888.txt)
NO_MATCH (i-DEfault) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-889.txt)
NO_MATCH (I-Lux) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-890.txt)
NO_MATCH (I-KLIngoN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-903.txt)
NO_MATCH (i-enOcHIaN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-906.txt)
NO_MATCH (I-tAO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-922.txt)
NO_MATCH (i-nAVAJo) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-923.txt)
NO_MATCH (i-aMI) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-948.txt)
NO_MATCH (sgn-BE-Fr) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-950.txt)
NO_MATCH (i-TAO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-951.txt)
NO_MATCH (I-MIngO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-959.txt)
NO_MATCH (i-Lux) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-969.txt)
NO_MATCH (I-Hak) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-970.txt)
NO_MATCH (i-BnN) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-971.txt)
NO_MATCH (i-TSU) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-974.txt)
NO_MATCH (i-NAvaJO) <- (tests/abnfgen/language-tag-n-1000-s-42-skip-1-100/language-tag-998.txt)
```
### Other Reports

Using only the first 100 test cases and a different external validator from Christoph Schneegans:

[https://schneegans.de/lv/?tags=X-Z...](https://schneegans.de/lv/?tags=X-Z%0D%0ANhr-826-x-37xd5v10-4-95G-4b0-McE-q-z-649-tJ-3232Sm-C-8%0D%0AI-TAO%0D%0Ax-sK-aT-QU-Xul-j-oif-IF%0D%0AwORgynep-VkYL-3WHP-DBAgB-cargOZkD-6jNC-YGpgM-dAhKA-7EZG-0Rrx-OZMlCbo-2vhf-5wkc-7OFG-wRKmQ-lGajd-3CKC-1Yrl-1FqL-7ztG-1gjk-z-xMFaehZZ%0D%0AEDuiK-naTz-Lo-B-4s-bXQn-351-75-1V-F04V-U2-53n-gw-Ot-c7-egjG-X-1%0D%0ArjuM-Ne-Z-gO-Tl-8-5UyR-x-02O6CWc%0D%0Ags-REm-9F57ro%0D%0AZH-XIANG%0D%0AoUr-7c8D-1t3E08-Y52Cr8-X-z%0D%0AZH-HAKKA%0D%0AZP-yhG-FzX-Znu-pqoK-073-6e82-9r8C-0wI8%0D%0AKXrXG-hQBc%0D%0Ai-tsu%0D%0ACvML-FazM-x-5%0D%0ALBwhXW-dQRH-599-Q-2Q0-x-aN%0D%0AI-PWN%0D%0AsgG-ppEv-0w6s-8Y86-W-4uW-0Cb-x-l%0D%0Atpxe-Ha-c-cY4-x-H-D-O-D-GxN64rG%0D%0AIlDcnl-vDct-Kf%0D%0AlN-BtU-PNV-GiB-8LOv-4I14-x-d-DY2w-R6%0D%0Ajm-VaA-0gEH1%0D%0Ai-ami%0D%0AIrzH-zfOI-103-y-tqnGh0%0D%0AZH-GUOYU%0D%0AztTF-M-G7%0D%0AART-LOJBAN%0D%0AkhzJ-x-5E-5%0D%0Azh-guoyu%0D%0Ano-bok%0D%0Asgn-be-fr%0D%0AoCt-HJe-oGtt-L-30U-F5-7l-Y-bI-C-98-X-7V6W2-ns%0D%0AzIrezey-zAvB-x-7-6%0D%0AWpGTR-Nz-pbign-X-q77%0D%0APTqo-124%0D%0AFkbev-Fbrz-oe-I-Q7-X-b%0D%0ASGN-BE-FR%0D%0AFK-mQu-WJs-crL-X-33-NuH893eK-N-9-6U2%0D%0AZH-MIN-NAN%0D%0AVJCq-mtKh-567p6-3b2r-l-86-x-26%0D%0ACEL-GAULISH%0D%0AIXdQbMDl-jal84-1R37%0D%0Aoxc-GXL-eIt-gsPP-zb-5053-N-23g-X-2%0D%0Azh-min%0D%0AlGnU-449-J0p3i836-6AxS-38Y41mt%0D%0AGGw-85Ee-H-16%0D%0AHqH-gxZU-451-u-wg4-d-5hK0%0D%0Acel-gaulish%0D%0Azh-xiang%0D%0AvBgj-XoTH-sh4ectk%0D%0ASGN-CH-DE%0D%0AZH-MIN%0D%0Ai-hak%0D%0AADTRG-324-Um924-1z85-34421-U-I772287-6a-13-fIwq6-n-rQ7-X-7p-ln44%0D%0AWQSm-MczP-Gg-2952-906p6-S-1Pv-Z9-I9y4-e-0w%0D%0ANO-BOK%0D%0AkA-rPb-npj-TCq-jX%0D%0Azh-min-nan%0D%0ARwdz-ngzf-577-46Jt54m8-22h3-78721-5f16-02zT-R-Pq20k-8l3-013i-0mT5N-eU-P347-m1-o-5a-x-1%0D%0Azh-hakka%0D%0AbwCu-TuLm-X-B-01-0-F-Kf%0D%0Asgn-ch-de%0D%0Aart-lojban%0D%0ATAiCvajp-wtia-101Jo9-6PY33K64-w-16-8wJ8%0D%0AQCnL-MJ-X-I%0D%0APz-yW%0D%0AI-HAK%0D%0ASGN-BE-NL%0D%0AtLCF-Oe-11qy-559c9v-k7nR94Ev-s-6VPx-1M-T-fb-t60K0-c1621X-1637-E-052-69-f4-p0-7qR-x-g%0D%0ATKq-aOFp-59tEt-904c-X-5m-84-ImZ%0D%0AI-MINGO%0D%0ANO-NYN%0D%0AOPLye-PAwd-Se-x-842-2%0D%0AI-TAY%0D%0Ano-nyn%0D%0AYhIlc-ReAB%0D%0Ai-default%0D%0Ai-tay%0D%0AUHV-Iifv-871-0vQ8-1o436TF-8H643-X-4-1U2V-5G-5-W-A2%0D%0AsDLW-Fs-X-ce76-M-N-8em%0D%0AiKy-Nsp-dLrJ-Lz-iylm5-P-Y0-V8%0D%0Ai-mingo%0D%0AI-NAVAJO%0D%0ABuXFIG-isvR-h-00-x-28-7%0D%0AI-TSU%0D%0AYF-bEC-XJV-Szsq-NZ-p-70-A-3B%0D%0AI-KLINGON%0D%0AAJ-yhH-eY%0D%0ATbuzXlz-fa-f-0S-U6-BI%0D%0Ai-pwn%0D%0AJpxKkOc-McbZ-141%0D%0AJp-NY%0D%0AEqiRNS-4316-0s57-9Ufq-X-9-k-w1-9F%0D%0AAIVRNKl-a-0wM17-k8-73%0D%0AI-ENOCHIAN%0D%0ALzx-uzi-AYU%0D%0AI-AMI%0D%0Ai-navajo%0D%0ANaTOKE-20yuw5u4-3HMh-Q0b6zT-V-xT6qg-XxC9-k-Q85-g-38-K-Y36m3-16JD-5k13R-M4zh%0D%0Ai-klingon&format=text)

A report of these first 100 test cases in JSON format as generated by schneegans.de validator is temporarily stored [here](report-1-100-schneegans-dot-de-report.json).


**Note**: The default branch is `default`.

