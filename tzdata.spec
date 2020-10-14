Name:		tzdata
Version:	2020b
Release:	2
Summary:	Timezone data
License:	Public Domain
URL:		https://www.iana.org/time-zones
Source0:	https://data.iana.org/time-zones/releases/tzdata%{version}.tar.gz
Source1:	https://data.iana.org/time-zones/releases/tzcode%{version}.tar.gz
Source2:	javazic.tar.gz
Source3:	javazic-1.8-37392f2f5d59.tar.xz

Patch6000:	backport-Fiji-observes-DST-from-2020-12-20-to-2021-01-17.patch
Patch6001:	backport-europe-Hungary-URL-comments-thanks-to-Michael-Decker.patch
Patch6002:	backport-ziguard.awk-Add-limitations-commentary.patch
Patch6003:	backport-Put-dummy-pacificnew-into-rearguard-tarball.patch
Patch6004:	backport-europe-Hungary-Add-more-URLs-thanks-to-G-za-Ny-ry.patch

Patch9000:	bugfix-0001-add-Beijing-timezone.patch
Patch9001: 	remove-country-selection-from-tzselect-steps.patch
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

%description java
This package contains timezone information for use by Java runtimes.

%prep
%autosetup -c -a 1 -p1

make VERSION=%{version} tzdata%{version}-rearguard.tar.gz
tar zxf tzdata%{version}-rearguard.tar.gz
rm tzdata.zi

mkdir javazic
tar zxf %{SOURCE2} -C javazic
cd javazic

mv sun rht
find . -type f -name '*.java' -print0 \
    | xargs -0 -- sed -i -e 's:sun\.tools\.:rht.tools.:g' \
                         -e 's:sun\.util\.:rht.util.:g'
cd ..

tar xf %{SOURCE3}

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
* Wed Oct 14 2020 liuchao<liuchao173@huawei.com> - 2020b-2
- backport community patches

* Sat Oct 10 2020 liuchao<liuchao173@huawei.com> - 2020b-1
- Upgrade to 2020b

* Wed Jun 17 2020 Shinwell Hu <huxinwei@huawei.com> - 2020a-1
- Upgrade to 2020a

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
