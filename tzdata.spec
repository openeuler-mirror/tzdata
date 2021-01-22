Name:		tzdata
Version:	2020a
Release:	10
Summary:	Timezone data
License:	Public Domain
URL:		https://www.iana.org/time-zones
Source0:	https://data.iana.org/time-zones/releases/tzdata%{version}.tar.gz
Source1:	https://data.iana.org/time-zones/releases/tzcode%{version}.tar.gz

Patch6001:	backport-Remove-tzsetwall.patch
Patch6002:	backport-Use-bold-for-command-and-func-names-in-man-pages.patch
Patch6003:	backport-Mention-TimeZoneDB-s-CSV-and-SQL-files.patch
Patch6004:	backport-More-Ruthenia-replacement.patch
Patch6005:	backport-Fix-comment-typo-re-1900-Spanish-decree.patch
Patch6006:	backport-Predict-Morocco-spring-forward-after-Eid-al-Fitr.patch
Patch6007:	backport-Fix-Hungarian-transitions-1918-1983.patch
Patch6008:	backport-Improve-1890-Hungarian-transition.patch
Patch6009:	backport-europe-Add-Hungaricana-URLs-thanks-to-G-za-Ny-ry.patch
Patch6010:	backport-French-clocks-stopped-for-9-21-on-1911-03-11.patch
Patch6011:	backport-Further-fixes-to-1891-and-1911-French-transitions.patch
Patch6012:	backport-NEWS-Fix-recent-date-typo.patch
Patch6013:	backport-Go-back-to-midnight-transitions-for-France-etc.patch
Patch6014:	backport-europe-Fix-minor-comment-typos-in-previous-change.patch
Patch6015:	backport-zic-has-new-l-and-p-options.patch
Patch6016:	backport-Do-not-install-posixrules-by-default.patch
Patch6017:	backport-zic-now-defaults-to-b-slim.patch
Patch6018:	backport-Cite-Mirmalek-on-Martian-timekeeping.patch
Patch6019:	backport-No-leap-second-on-2020-12-31.patch
Patch6020:	backport-Fix-leapseconds-comment-when-EXPIRES_LINE.patch
Patch6021:	backport-Update-Bahrain-as-per-article-in-The-National.patch
Patch6022:	backport-backzone-More-commentary-re-1940s-Bahrain.patch
Patch6023:	backport-Minor-editorial-improvements-for-newstrftime.3.patch
Patch6024:	backport-strftime-conform-better-to-POSIX.patch
Patch6025:	backport-date-redo-strftime-buffer-exhaustion-check.patch
Patch6026:	backport-date-simplify-format-compuation.patch
Patch6027:	backport-README-Add-a-pointer-to-tz-how-to.html.patch
Patch6028:	backport-Mention-Intl.DateTimeFormat.patch
Patch6029:	backport-asia-Cite-Barak-2020-on-Israeli-DST-controversy.patch
Patch6030:	backport-Cite-Rishi-et-al-in-tz-link.patch
Patch6031:	backport-tz-link.html-Cite-TZDIST-list.-Thanks-to-Michael-Dou.patch
Patch6032:	backport-Improve-heads-up-advice.patch
Patch6033:	backport-tz-art.html-Add-Mr.-Monk-thanks-to-Arthur-David-Olso.patch
Patch6034:	backport-tz-link.html-Cite-Python-3.9-thanks-to-Matt-Johnson-.patch
Patch6035:	backport-tz-link.html-Cite-PyPI-tzdata-thanks-to-Paul-Ganssle.patch
Patch6036:	backport-Yukon-s-change-is-effective-2020-11-01.patch
Patch6037:	backport-NEWS-Fix-typo-thanks-to-Philip-Paeps.patch
Patch6038:	backport-Fixes-for-Casey-and-Macquarie.patch
Patch6039:	backport-antarctica-Antarctica-Casey-Correct-2019-10-transiti.patch
Patch6040:	backport-Remove-obsolete-file-systemv.patch
Patch6041:	backport-Drop-support-for-zic-y-Rule-TYPEs-pacificnew.patch
Patch6042:	backport-Further-update-code-to-match-Link-line-field-names.patch
Patch6043:	backport-Convert-tz-how-to.html-to-HTML-5.patch
Patch6044:	backport-Tighten-up-scope-wording.patch
Patch6045:	backport-NEWS-Fix-Antarctic-seasons-Casey-change-is-past.patch
Patch6046:	backport-Release-2020b.patch
Patch6047:	backport-Fiji-observes-DST-from-2020-12-20-to-2021-01-17.patch
Patch6048:	backport-europe-Hungary-URL-comments-thanks-to-Michael-Decker.patch
Patch6049:	backport-ziguard.awk-Add-limitations-commentary.patch
Patch6050:	backport-Put-dummy-pacificnew-into-rearguard-tarball.patch
Patch6051:	backport-europe-Hungary-Add-more-URLs-thanks-to-G-za-Ny-ry.patch
Patch6052:	backport-Release-2020c.patch
Patch6053:	backport-Update-Danish-URLs.patch
Patch6054:	backport-Cite-Tom-Scott-on-Danish-time.patch
Patch6055:	backport-Port-make-rearguard_tarballs-to-macOS.patch
Patch6056:	backport-Improve-TZUpdater-and-Python-links.patch
Patch6057:	backport-Fail-on-ZIC_BLOAT_DEFAULT-typo.patch
Patch6058:	backport-Palestine-ends-DST-on-2020-10-24.patch
Patch6059:	backport-Fix-Palestine-2015-fall-and-2020-spring.patch
Patch6060:	backport-tz-link.html-Fix-typo.patch
Patch6061:	backport-Release-2020d.patch
Patch6062:	backport-Port-to-downstream-HP-UX-style-make.patch
Patch6063:	backport-etcetera-Update-comment-in-the-light-of-Neil-Fuller-.patch
Patch6064:	backport-Use-better-fallback-for-unknown-VERSION.patch
Patch6065:	backport-Fix-Kenya-transitions-1908-1960.patch
Patch6066:	backport-leapseconds-now-says-why-NIST-not-IERS.patch
Patch6067:	backport-Fix-zone-.tab-Yukon-comment-columns.patch
Patch6068:	backport-Fix-Israel-and-Palestine-transitions-1940-1985.patch
Patch6069:	backport-Port-make-rearguard_tarballs-to-Solaris-10.patch
Patch6070:	backport-Fix-several-Belize-transitions-1942-1968.patch
Patch6071:	backport-Fix-mistaken-Belize-interpretation.patch
Patch6072:	backport-Document-right-seconds-better.patch
Patch6073:	backport-tz-link.html-Use-abbr-more-systematically.patch
Patch6074:	backport-Fix-several-pre-1972-transitions-for-Australia.patch
Patch6075:	backport-Fix-several-pre-1957-transitions-for-Bermuda.patch
Patch6076:	backport-Fix-several-pre-1957-transitions-for-Ghana.patch
Patch6077:	backport-northamerica-Add-URL-for-Yukon-OIC-1980-02.patch
Patch6078:	backport-Volgograd-switches-from-04-to-03-on-12-20-02-00.patch
Patch6079:	backport-Fix-Ghana-typo-for-1919-1920.patch
Patch6080:	backport-Re-fix-Ghana-typo-for-1919-1920.patch
Patch6081:	backport-Fix-several-pre-1946-transitions-for-Bahamas.patch
Patch6082:	backport-Fix-Volgograd-label-in-zone-zone1970-.tab.patch
Patch6083:	backport-Fix-Ghana-again-for-1942-through-1946.patch
Patch6084:	backport-Fix-some-errors-in-recent-Bahamas-changes.patch
Patch6085:	backport-Volgograd-change-likely-December-27-not-20.patch
Patch6086:	backport-Fix-Vanuatu-DST-in-1973-1974-and-1984-transition.patch
Patch6087:	backport-Model-Turks-Caicos-time-2015-2018-as-AST.patch
Patch6088:	backport-Seychelles-switched-from-LMT-to-04-on-1907-01-01.patch
Patch6089:	backport-Document-zic-coalescing-zone-DST-transitions.patch
Patch6090:	backport-Fix-NEWS-typo.patch
Patch6091:	backport-Correct-LMT-and-pre-1919-transitions-for-Nigeria.patch
Patch6092:	backport-Cite-publication-of-Volgograd-change.patch
Patch6093:	backport-Improve-doc-of-zic-coalescing-zone-DST-transitions.patch
Patch6094:	backport-Release-2020e.patch
Patch6095:	backport-Fix-rearguard.zi-corruption-in-2020e.patch
Patch6096:	backport-Release-2020f.patch
Patch6097:	backport-No-leap-second-on-2021-06-30.patch
Patch6098:	backport-South-Sudan-changes-from-03-to-02-on-2021-02-01.patch

Patch9000:	bugfix-0001-add-Beijing-timezone.patch
Patch9001:	remove-country-selection-from-tzselect-steps.patch
Patch9002:	remove-ROC-timezone.patch
Patch9003:	rename-Macau-to-Macao.patch
Patch9004:	remove-El_Aaiun-timezone.patch
Patch9005:	remove-Israel-timezone.patch

BuildRequires:	gawk glibc perl-interpreter
BuildRequires:	java-devel
BuildRequires:	glibc-common >= 2.5.90-7
BuildArchitectures: noarch

%description
This package contains data files with rules for various timezones around
the world.

%package        java
Summary:	Timezone data for Java
Source3:	javazic.tar.gz
Source4:	javazic-1.8-37392f2f5d59.tar.xz

%description java
This package contains timezone information for use by Java runtimes.

%prep
%autosetup -c -a 1 -p1

make VERSION=%{version} tzdata%{version}-rearguard.tar.gz
tar zxf tzdata%{version}-rearguard.tar.gz
rm tzdata.zi

mkdir javazic
tar zxf %{SOURCE3} -C javazic
cd javazic

mv sun rht
find . -type f -name '*.java' -print0 \
    | xargs -0 -- sed -i -e 's:sun\.tools\.:rht.tools.:g' \
                         -e 's:sun\.util\.:rht.util.:g'
cd ..

tar xf %{SOURCE4}

echo "%{name}%{version}" >> VERSION

%build
make VERSION=%{version} DATAFORM=rearguard tzdata.zi

FILES="africa antarctica asia australasia europe northamerica southamerica
       etcetera backward"

mkdir zoneinfo/{,posix,right}
zic -y ./yearistype -d zoneinfo -L /dev/null -p America/New_York $FILES
zic -y ./yearistype -d zoneinfo/posix -L /dev/null $FILES
zic -y ./yearistype -d zoneinfo/right -L leapseconds $FILES

cd javazic
javac -source 1.5 -target 1.5 -classpath . `find . -name \*.java`
cd ..

java -classpath javazic/ rht.tools.javazic.Main -V %{version} \
  -d javazi \
  $FILES javazic/tzdata_jdk/gmt javazic/tzdata_jdk/jdk11_backward

cd javazic-1.8
javac -source 1.7 -target 1.7 -classpath . `find . -name \*.java`
cd ..

java -classpath javazic-1.8 build.tools.tzdb.TzdbZoneRulesCompiler \
    -srcdir . -dstfile tzdb.dat \
    -verbose \
    $FILES javazic-1.8/tzdata_jdk/gmt javazic-1.8/tzdata_jdk/jdk11_backward

%install

rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}
cp -prd zoneinfo $RPM_BUILD_ROOT%{_datadir}
install -p -m 644 zone.tab zone1970.tab iso3166.tab leapseconds tzdata.zi $RPM_BUILD_ROOT%{_datadir}/zoneinfo
cp -prd javazi $RPM_BUILD_ROOT%{_datadir}/javazi
mkdir -p $RPM_BUILD_ROOT%{_datadir}/javazi-1.8
install -p -m 644 tzdb.dat $RPM_BUILD_ROOT%{_datadir}/javazi-1.8/

%files
%{_datadir}/zoneinfo
%doc README
%doc theory.html
%doc tz-link.html
%doc tz-art.html
%license LICENSE

%files java
%{_datadir}/javazi
%{_datadir}/javazi-1.8

%changelog
* Fri Jan 22 2021 liuchao<liuchao173@huawei.com> - 2020a-10
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:backport community patches

* Mon Dec 7 2020 liuchao<liuchao173@huawei.com> - 2020a-9
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:backport community patches

* Mon Nov 30 2020 liuchao<liuchao173@huawei.com> - 2020a-8
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:backport community patches

* Tue Oct 27 2020 EulerOSWander<314264452@qq.com> - 2020a-7
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:backport upstream patches

* Tue Oct 27 2020 EulerOSWander<314264452@qq.com> - 2020a-6
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:backport upstream patches

* Thu Oct 22 2020 liuchao<liuchao173@huawei.com> - 2020a-5
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:backport community patches

* Wed Oct 21 2020 liuchao<liuchao173@huawei.com> - 2020a-4
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:backport community patches

* Wed Oct 14 2020 liuchao<liuchao173@huawei.com> - 2020a-3
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:backport community patches

* Sat Oct 10 2020 liuchao<liuchao173@huawei.com> - 2020a-2
- Type:recommended
- CVE:NA
- SUG:NA
- DESC:sync community patches

* Thu Jun 11 2020 liuchao<liuchao173@huawei.com> - 2020a-1
- Type:recommended
- ID:NA
- SUG:NA
- DESC:rebase to tzdata-2020a

* Thu Apr 16 2020 liuchao<liuchao173@huawei.com> - 2019c-1
- Type:recommended
- ID:NA
- SUG:NA
- DESC:rebase to tzdata-2019c

* Mon Mar 23 2020 liuchao<liuchao173@huawei.com> - 2019b-10
- Type:recommended
- ID:NA
- SUG:NA
- DESC:add Beijing timezone in zone1970.tab

* Thu Jan 9 2020 liuchao<liuchao173@huawei.com> - 2019b-9
- Type:recommended
- ID:NA
- SUG:NA
- DESC:remove useless patches

* Wed Jan 8 2020 liuchao<liuchao173@huawei.com> - 2019b-8
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:remove Israel and El_Aaiun timezone

* Thu Jan 2 2020 liuchao<liuchao173@huawei.com> - 2019b-7
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:sync community patches

* Wed Dec 4 2019 liuchao<liuchao173@huawei.com> - 2019b-6
- Type:recommended
- ID:NA
- SUG:NA
- DESC:remove ROC timezone and rename Macau to Macao

* Mon Sep 23 2019 liuchao<liuchao173@huawei.com> -2019b-5
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: use rearguard data set to fix Casablance DST display error since 2019

* Wed Sep 4 2019 hejingxian<hejingxian@huawei.com> - 2019b-4
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: remove  country select operation from tzselect steps.

* Fri Aug 23 2019 wuxu<wuxu.wu@huawei.com> - 2019b-3
- Type:recommended
- ID:NA
- SUG:NA

* Thu Jul 25 2019 luochunsheng<luochunsheng@huawei.com> - 2019b-2
- Type:recommended
- ID:NA
- SUG:NA

* Tue Jul 09 2019 openEuler Buildteam <buildteam@openeuler.org> - 2019b-1
- Rebase to tzdata-2019b
  - Brazil will no longer observe DST going forward.
  - The 2019 spring transition for Palestine occurred 03-29, not 03-30.

* Sun May 5 2019 luochunsheng<luochunsheng@huawei.com> - 2019a-4
- Type:fix
- ID:NA
- SUG:NA
- DESC: Bring back 2019-2037 Morocco Ramadan predictions
	https://www.timeanddate.com/news/time/morocco-changes-clocks-2019.html

* Mon Apr 22 2019 luochunsheng<luochunsheng@huawei.com> - 2019a-3
- Type:NA
- ID:NA
- SUG:NA
- DESC: Revert "Bring back 2019-2037 Morocco Ramadan predictions" to
	 fix Morocco zoneinfo.

* Wed Apr 17 2019 luochunsheng<luochunsheng@huawei.com> - 2019a-2
- Type:NA
- ID:NA
- SUG:NA
- DESC:Quality enhance

* Fri Mar 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 2019a-1
- Rebase to tzdata-2019a
  - Palestine will start DST on 2019-03-30, rather than 2019-03-23 as
    previously predicted.
  - Metlakatla rejoined Alaska time on 2019-01-20, ending its observances
    of Pacific standard time.

* Fri Mar 8 2019 wangjia<wangjia55@huawei.com> - 2018i-2
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add Beijing timezone

* Tue Jan 15 2019 openEuler Buildteam <buildteam@openeuler.org> - 2018i-1
- Package init
