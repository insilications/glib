#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : glib
Version  : 2.71.0
Release  : 324
URL      : file:///aot/build/clearlinux/packages/glib/glib-v2.71.0.tar.gz
Source0  : file:///aot/build/clearlinux/packages/glib/glib-v2.71.0.tar.gz
Source1  : glib-schemas-firstboot.service
Source2  : glib-schemas-trigger.service
Source3  : glib.tmpfiles
Summary  : Common C routines used by Gtk+ and other libs
Group    : Development/Tools
License  : LGPL-2.0+ LGPL-2.1
Requires: glib-autostart = %{version}-%{release}
Requires: glib-bin = %{version}-%{release}
Requires: glib-config = %{version}-%{release}
Requires: glib-data = %{version}-%{release}
Requires: glib-lib = %{version}-%{release}
Requires: glib-libexec = %{version}-%{release}
Requires: glib-locales = %{version}-%{release}
Requires: glib-man = %{version}-%{release}
Requires: glib-services = %{version}-%{release}
Requires: shared-mime-info
BuildRequires : attr
BuildRequires : attr-dev
BuildRequires : attr-dev32
BuildRequires : attrs
BuildRequires : bash-completion-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dbus-broker
BuildRequires : dbus-dev
BuildRequires : dbus-dev32
BuildRequires : dbus-extras
BuildRequires : dbus-glib-dev
BuildRequires : dbus-python
BuildRequires : desktop-file-utils
BuildRequires : docbook-xml
BuildRequires : elfutils-dev
BuildRequires : elfutils-dev32
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gettext
BuildRequires : glib-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : libffi-dev
BuildRequires : libffi-dev32
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libxml2-dev
BuildRequires : libxml2-dev32
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pcre-dev
BuildRequires : pcre-dev32
BuildRequires : pcre-staticdev
BuildRequires : perl
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(libelf)
BuildRequires : shared-mime-info
BuildRequires : systemd-dev
BuildRequires : systemd-dev32
BuildRequires : tzdata
BuildRequires : util-linux-dev
BuildRequires : util-linux-dev32
BuildRequires : util-linux-staticdev
BuildRequires : which
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-gio-Support-a-stateless-configuration-for-compiled-G.patch
Patch2: 0002-xdg-path.patch
Patch3: 0003-wakeups.patch
Patch4: 0004-gerror-return-on-null.patch
Patch5: 0005-gmodule-avx.patch
Patch6: 0006-Include-a-new-stub-header-to-help-with-multilib-comp.patch
Patch7: 0007-Check-for-32bit-linker-flag-when-creating-resource-f.patch
Patch8: 0008-Disable-use-of-close_range.patch

%description
GLib provides the core application building blocks for libraries and
applications written in C. It provides the core object system used in GNOME,
the main loop implementation, and a large set of utility functions for strings
and common data structures.

%package autostart
Summary: autostart components for the glib package.
Group: Default

%description autostart
autostart components for the glib package.


%package bin
Summary: bin components for the glib package.
Group: Binaries
Requires: glib-data = %{version}-%{release}
Requires: glib-libexec = %{version}-%{release}
Requires: glib-config = %{version}-%{release}
Requires: glib-services = %{version}-%{release}

%description bin
bin components for the glib package.


%package config
Summary: config components for the glib package.
Group: Default

%description config
config components for the glib package.


%package data
Summary: data components for the glib package.
Group: Data

%description data
data components for the glib package.


%package dev
Summary: dev components for the glib package.
Group: Development
Requires: glib-lib = %{version}-%{release}
Requires: glib-bin = %{version}-%{release}
Requires: glib-data = %{version}-%{release}
Provides: glib-devel = %{version}-%{release}
Requires: glib = %{version}-%{release}

%description dev
dev components for the glib package.


%package dev32
Summary: dev32 components for the glib package.
Group: Default
Requires: glib-lib32 = %{version}-%{release}
Requires: glib-bin = %{version}-%{release}
Requires: glib-data = %{version}-%{release}
Requires: glib-dev = %{version}-%{release}

%description dev32
dev32 components for the glib package.


%package lib
Summary: lib components for the glib package.
Group: Libraries
Requires: glib-data = %{version}-%{release}
Requires: glib-libexec = %{version}-%{release}

%description lib
lib components for the glib package.


%package lib32
Summary: lib32 components for the glib package.
Group: Default
Requires: glib-data = %{version}-%{release}

%description lib32
lib32 components for the glib package.


%package libexec
Summary: libexec components for the glib package.
Group: Default
Requires: glib-config = %{version}-%{release}

%description libexec
libexec components for the glib package.


%package locales
Summary: locales components for the glib package.
Group: Default

%description locales
locales components for the glib package.


%package man
Summary: man components for the glib package.
Group: Default

%description man
man components for the glib package.


%package services
Summary: services components for the glib package.
Group: Systemd services

%description services
services components for the glib package.


%package staticdev
Summary: staticdev components for the glib package.
Group: Default
Requires: glib-dev = %{version}-%{release}

%description staticdev
staticdev components for the glib package.


%package staticdev32
Summary: staticdev32 components for the glib package.
Group: Default
Requires: glib-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the glib package.


%prep
%setup -q -n glib
cd %{_builddir}/glib
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
pushd %{_builddir}
cp -a %{_builddir}/glib build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1642239722
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
## altflags1 content
## altflags1
unset ASFLAGS
export CFLAGS="-ggdb3 -ggnu-pubnames -Ofast -mvzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export ASMFLAGS="-ggdb3 -ggnu-pubnames -Ofast -mvzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export CXXFLAGS="-ggdb3 -ggnu-pubnames -Ofast -mvzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FCFLAGS="-ggdb3 -ggnu-pubnames -Ofast -mvzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-ggdb3 -ggnu-pubnames -Ofast -mvzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -fexceptions -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export LDFLAGS="-ggdb3 -ggnu-pubnames -Ofast -mvzeroupper --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code -Wno-error -mprefer-vector-width=256 -falign-functions=32 -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -Wl,-Bsymbolic-functions -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-slp-vectorize -ftree-vectorize -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flive-range-shrinkage -flto=auto -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -fomit-frame-pointer -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
export MAKEFLAGS=%{?_smp_mflags}
%global _lto_cflags 1
%global _disable_maintainer_mode 1
export CCACHE_DISABLE=true
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:/usr/share/pkgconfig"
export LD_LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export LIBRARY_PATH="/usr/local/nvidia/lib64:/usr/local/nvidia/lib64/gbm:/usr/local/nvidia/lib64/vdpau:/usr/local/nvidia/lib64/xorg/modules/drivers:/usr/local/nvidia/lib64/xorg/modules/extensions:/usr/local/cuda/lib64:/usr/lib64/haswell:/usr/lib64/dri:/usr/lib64:/usr/lib:/aot/intel/oneapi/compiler/latest/linux/compiler/lib/intel64_lin:/aot/intel/oneapi/compiler/latest/linux/lib:/aot/intel/oneapi/mkl/latest/lib/intel64:/aot/intel/oneapi/tbb/latest/lib/intel64/gcc4.8:/usr/share:/usr/lib64/wine:/usr/local/nvidia/lib32:/usr/local/nvidia/lib32/vdpau:/usr/lib32:/usr/lib32/wine"
export PATH="/usr/lib64/ccache/bin:/usr/local/cuda/bin:/usr/local/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export CPATH="/usr/local/cuda/include"
export DISPLAY=:0
export __GL_SYNC_TO_VBLANK=1
export __GL_SYNC_DISPLAY_DEVICE=HDMI-0
export VDPAU_NVIDIA_SYNC_DISPLAY_DEVICE=HDMI-0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH="/usr/share/defaults/fonts"
export GTK_IM_MODULE="xim"
export QT_IM_MODULE="cedilla"
export FREETYPE_PROPERTIES="truetype:interpreter-version=40"
export NO_AT_BRIDGE=1
export GTK_A11Y=none
export PLASMA_USE_QT_SCALING=1
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_ENABLE_HIGHDPI_SCALING=0
export QT_FONT_DPI=88
export GTK_USE_PORTAL=1
export DESKTOP_SESSION=plasma
export GSETTINGS_SCHEMA_DIR="/usr/share/glib-2.0/schemas"
## altflags1 end
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" LIBS="$LIBS" meson --libdir=lib64 --sysconfdir=/usr/share --prefix=/usr --buildtype=plain -Ddefault_library=both  -Dglib_assert=false \
-Dglib_debug=disabled \
-Dman=true \
-Dgio_module_dir="/usr/lib64/gio/modules" \
-Dselinux=disabled \
-Dnls=enabled \
-Dxattr=true \
-Dlibmount=enabled \
-Dbsymbolic_functions=true \
-Dinstalled_tests=false \
-Dtests=true builddir
ninja --verbose %{?_smp_mflags} -C builddir


pushd ../build32/
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
unset LIBRARY_PATH
unset CPATH
unset ASFLAGS
unset CFLAGS
unset CXXFLAGS
unset FCFLAGS
unset FFLAGS
unset LDFLAGS
unset LINKFLAGS
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="--32"
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export ASMFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FCFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export FFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -march=native -mtune=native -m32 -mstackrealign"
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" LIBS="$LIBS" meson --libdir=lib32 --sysconfdir=/usr/share --prefix=/usr --buildtype=plain -Ddefault_library=both  -Dinstalled_tests=false \
-Dglib_assert=false \
-Dglib_checks=true \
-Dgio_module_dir="/usr/lib32/gio/modules" builddir
ninja --verbose %{?_smp_mflags} -C builddir

popd

%install
pushd ../build32/
DESTDIR=%{buildroot} ninja -C builddir install

if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
DESTDIR=%{buildroot} ninja -C builddir install

%find_lang glib20
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/glib-schemas-firstboot.service
install -m 0644 %{SOURCE2} %{buildroot}/usr/lib/systemd/system/glib-schemas-trigger.service
mkdir -p %{buildroot}/usr/lib/tmpfiles.d
install -m 0644 %{SOURCE3} %{buildroot}/usr/lib/tmpfiles.d/glib.conf
## install_append content
# enable the glib schema compile trigger
mkdir -p %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants
ln -s /usr/lib/systemd/system/glib-schemas-trigger.service %{buildroot}/usr/lib/systemd/system/update-triggers.target.wants/glib-schemas-trigger.service
# also enable glib schema compile on first boot
mkdir -p %{buildroot}/usr/lib/systemd/system/graphical.target.wants
ln -s /usr/lib/systemd/system/glib-schemas-firstboot.service %{buildroot}/usr/lib/systemd/system/graphical.target.wants/glib-schemas-firstboot.service

# place it in libexec (with compat)
mkdir -p %{buildroot}/usr/libexec
mv %{buildroot}/usr/bin/glib-compile-schemas %{buildroot}/usr/libexec/glib-compile-schemas
ln -s ../libexec/glib-compile-schemas %{buildroot}/usr/bin

# fix busted multlib compiles by providing custom header to include the right architecture file
install -m 00644 multilib-glibconfig.h %{buildroot}/usr/include/glib-2.0/glibconfig.h
## install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/graphical.target.wants/glib-schemas-firstboot.service

%files bin
%defattr(-,root,root,-)
/usr/bin/gapplication
/usr/bin/gdbus
/usr/bin/gdbus-codegen
/usr/bin/gio
/usr/bin/gio-querymodules
/usr/bin/glib-compile-resources
/usr/bin/glib-compile-schemas
/usr/bin/glib-genmarshal
/usr/bin/glib-gettextize
/usr/bin/glib-mkenums
/usr/bin/gobject-query
/usr/bin/gresource
/usr/bin/gsettings
/usr/bin/gtester
/usr/bin/gtester-report

%files config
%defattr(-,root,root,-)
/usr/lib/tmpfiles.d/glib.conf

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/gapplication
/usr/share/bash-completion/completions/gdbus
/usr/share/bash-completion/completions/gio
/usr/share/bash-completion/completions/gresource
/usr/share/bash-completion/completions/gsettings
/usr/share/gettext/its/gschema.its
/usr/share/gettext/its/gschema.loc
/usr/share/glib-2.0/codegen/__init__.py
/usr/share/glib-2.0/codegen/codegen.py
/usr/share/glib-2.0/codegen/codegen_docbook.py
/usr/share/glib-2.0/codegen/codegen_main.py
/usr/share/glib-2.0/codegen/config.py
/usr/share/glib-2.0/codegen/dbustypes.py
/usr/share/glib-2.0/codegen/parser.py
/usr/share/glib-2.0/codegen/utils.py
/usr/share/glib-2.0/gdb/glib_gdb.py
/usr/share/glib-2.0/gdb/gobject_gdb.py
/usr/share/glib-2.0/gettext/po/Makefile.in.in
/usr/share/glib-2.0/schemas/gschema.dtd
/usr/share/glib-2.0/valgrind/glib.supp

%files dev
%defattr(-,root,root,-)
/usr/include/gio-unix-2.0/gio/gdesktopappinfo.h
/usr/include/gio-unix-2.0/gio/gfiledescriptorbased.h
/usr/include/gio-unix-2.0/gio/gunixconnection.h
/usr/include/gio-unix-2.0/gio/gunixcredentialsmessage.h
/usr/include/gio-unix-2.0/gio/gunixfdlist.h
/usr/include/gio-unix-2.0/gio/gunixfdmessage.h
/usr/include/gio-unix-2.0/gio/gunixinputstream.h
/usr/include/gio-unix-2.0/gio/gunixmounts.h
/usr/include/gio-unix-2.0/gio/gunixoutputstream.h
/usr/include/gio-unix-2.0/gio/gunixsocketaddress.h
/usr/include/glib-2.0/gio/gaction.h
/usr/include/glib-2.0/gio/gactiongroup.h
/usr/include/glib-2.0/gio/gactiongroupexporter.h
/usr/include/glib-2.0/gio/gactionmap.h
/usr/include/glib-2.0/gio/gappinfo.h
/usr/include/glib-2.0/gio/gapplication.h
/usr/include/glib-2.0/gio/gapplicationcommandline.h
/usr/include/glib-2.0/gio/gasyncinitable.h
/usr/include/glib-2.0/gio/gasyncresult.h
/usr/include/glib-2.0/gio/gbufferedinputstream.h
/usr/include/glib-2.0/gio/gbufferedoutputstream.h
/usr/include/glib-2.0/gio/gbytesicon.h
/usr/include/glib-2.0/gio/gcancellable.h
/usr/include/glib-2.0/gio/gcharsetconverter.h
/usr/include/glib-2.0/gio/gcontenttype.h
/usr/include/glib-2.0/gio/gconverter.h
/usr/include/glib-2.0/gio/gconverterinputstream.h
/usr/include/glib-2.0/gio/gconverteroutputstream.h
/usr/include/glib-2.0/gio/gcredentials.h
/usr/include/glib-2.0/gio/gdatagrambased.h
/usr/include/glib-2.0/gio/gdatainputstream.h
/usr/include/glib-2.0/gio/gdataoutputstream.h
/usr/include/glib-2.0/gio/gdbusactiongroup.h
/usr/include/glib-2.0/gio/gdbusaddress.h
/usr/include/glib-2.0/gio/gdbusauthobserver.h
/usr/include/glib-2.0/gio/gdbusconnection.h
/usr/include/glib-2.0/gio/gdbuserror.h
/usr/include/glib-2.0/gio/gdbusinterface.h
/usr/include/glib-2.0/gio/gdbusinterfaceskeleton.h
/usr/include/glib-2.0/gio/gdbusintrospection.h
/usr/include/glib-2.0/gio/gdbusmenumodel.h
/usr/include/glib-2.0/gio/gdbusmessage.h
/usr/include/glib-2.0/gio/gdbusmethodinvocation.h
/usr/include/glib-2.0/gio/gdbusnameowning.h
/usr/include/glib-2.0/gio/gdbusnamewatching.h
/usr/include/glib-2.0/gio/gdbusobject.h
/usr/include/glib-2.0/gio/gdbusobjectmanager.h
/usr/include/glib-2.0/gio/gdbusobjectmanagerclient.h
/usr/include/glib-2.0/gio/gdbusobjectmanagerserver.h
/usr/include/glib-2.0/gio/gdbusobjectproxy.h
/usr/include/glib-2.0/gio/gdbusobjectskeleton.h
/usr/include/glib-2.0/gio/gdbusproxy.h
/usr/include/glib-2.0/gio/gdbusserver.h
/usr/include/glib-2.0/gio/gdbusutils.h
/usr/include/glib-2.0/gio/gdrive.h
/usr/include/glib-2.0/gio/gdtlsclientconnection.h
/usr/include/glib-2.0/gio/gdtlsconnection.h
/usr/include/glib-2.0/gio/gdtlsserverconnection.h
/usr/include/glib-2.0/gio/gemblem.h
/usr/include/glib-2.0/gio/gemblemedicon.h
/usr/include/glib-2.0/gio/gfile.h
/usr/include/glib-2.0/gio/gfileattribute.h
/usr/include/glib-2.0/gio/gfileenumerator.h
/usr/include/glib-2.0/gio/gfileicon.h
/usr/include/glib-2.0/gio/gfileinfo.h
/usr/include/glib-2.0/gio/gfileinputstream.h
/usr/include/glib-2.0/gio/gfileiostream.h
/usr/include/glib-2.0/gio/gfilemonitor.h
/usr/include/glib-2.0/gio/gfilenamecompleter.h
/usr/include/glib-2.0/gio/gfileoutputstream.h
/usr/include/glib-2.0/gio/gfilterinputstream.h
/usr/include/glib-2.0/gio/gfilteroutputstream.h
/usr/include/glib-2.0/gio/gicon.h
/usr/include/glib-2.0/gio/ginetaddress.h
/usr/include/glib-2.0/gio/ginetaddressmask.h
/usr/include/glib-2.0/gio/ginetsocketaddress.h
/usr/include/glib-2.0/gio/ginitable.h
/usr/include/glib-2.0/gio/ginputstream.h
/usr/include/glib-2.0/gio/gio-autocleanups.h
/usr/include/glib-2.0/gio/gio.h
/usr/include/glib-2.0/gio/gioenums.h
/usr/include/glib-2.0/gio/gioenumtypes.h
/usr/include/glib-2.0/gio/gioerror.h
/usr/include/glib-2.0/gio/giomodule.h
/usr/include/glib-2.0/gio/gioscheduler.h
/usr/include/glib-2.0/gio/giostream.h
/usr/include/glib-2.0/gio/giotypes.h
/usr/include/glib-2.0/gio/glistmodel.h
/usr/include/glib-2.0/gio/gliststore.h
/usr/include/glib-2.0/gio/gloadableicon.h
/usr/include/glib-2.0/gio/gmemoryinputstream.h
/usr/include/glib-2.0/gio/gmemorymonitor.h
/usr/include/glib-2.0/gio/gmemoryoutputstream.h
/usr/include/glib-2.0/gio/gmenu.h
/usr/include/glib-2.0/gio/gmenuexporter.h
/usr/include/glib-2.0/gio/gmenumodel.h
/usr/include/glib-2.0/gio/gmount.h
/usr/include/glib-2.0/gio/gmountoperation.h
/usr/include/glib-2.0/gio/gnativesocketaddress.h
/usr/include/glib-2.0/gio/gnativevolumemonitor.h
/usr/include/glib-2.0/gio/gnetworkaddress.h
/usr/include/glib-2.0/gio/gnetworking.h
/usr/include/glib-2.0/gio/gnetworkmonitor.h
/usr/include/glib-2.0/gio/gnetworkservice.h
/usr/include/glib-2.0/gio/gnotification.h
/usr/include/glib-2.0/gio/goutputstream.h
/usr/include/glib-2.0/gio/gpermission.h
/usr/include/glib-2.0/gio/gpollableinputstream.h
/usr/include/glib-2.0/gio/gpollableoutputstream.h
/usr/include/glib-2.0/gio/gpollableutils.h
/usr/include/glib-2.0/gio/gpowerprofilemonitor.h
/usr/include/glib-2.0/gio/gpropertyaction.h
/usr/include/glib-2.0/gio/gproxy.h
/usr/include/glib-2.0/gio/gproxyaddress.h
/usr/include/glib-2.0/gio/gproxyaddressenumerator.h
/usr/include/glib-2.0/gio/gproxyresolver.h
/usr/include/glib-2.0/gio/gremoteactiongroup.h
/usr/include/glib-2.0/gio/gresolver.h
/usr/include/glib-2.0/gio/gresource.h
/usr/include/glib-2.0/gio/gseekable.h
/usr/include/glib-2.0/gio/gsettings.h
/usr/include/glib-2.0/gio/gsettingsbackend.h
/usr/include/glib-2.0/gio/gsettingsschema.h
/usr/include/glib-2.0/gio/gsimpleaction.h
/usr/include/glib-2.0/gio/gsimpleactiongroup.h
/usr/include/glib-2.0/gio/gsimpleasyncresult.h
/usr/include/glib-2.0/gio/gsimpleiostream.h
/usr/include/glib-2.0/gio/gsimplepermission.h
/usr/include/glib-2.0/gio/gsimpleproxyresolver.h
/usr/include/glib-2.0/gio/gsocket.h
/usr/include/glib-2.0/gio/gsocketaddress.h
/usr/include/glib-2.0/gio/gsocketaddressenumerator.h
/usr/include/glib-2.0/gio/gsocketclient.h
/usr/include/glib-2.0/gio/gsocketconnectable.h
/usr/include/glib-2.0/gio/gsocketconnection.h
/usr/include/glib-2.0/gio/gsocketcontrolmessage.h
/usr/include/glib-2.0/gio/gsocketlistener.h
/usr/include/glib-2.0/gio/gsocketservice.h
/usr/include/glib-2.0/gio/gsrvtarget.h
/usr/include/glib-2.0/gio/gsubprocess.h
/usr/include/glib-2.0/gio/gsubprocesslauncher.h
/usr/include/glib-2.0/gio/gtask.h
/usr/include/glib-2.0/gio/gtcpconnection.h
/usr/include/glib-2.0/gio/gtcpwrapperconnection.h
/usr/include/glib-2.0/gio/gtestdbus.h
/usr/include/glib-2.0/gio/gthemedicon.h
/usr/include/glib-2.0/gio/gthreadedsocketservice.h
/usr/include/glib-2.0/gio/gtlsbackend.h
/usr/include/glib-2.0/gio/gtlscertificate.h
/usr/include/glib-2.0/gio/gtlsclientconnection.h
/usr/include/glib-2.0/gio/gtlsconnection.h
/usr/include/glib-2.0/gio/gtlsdatabase.h
/usr/include/glib-2.0/gio/gtlsfiledatabase.h
/usr/include/glib-2.0/gio/gtlsinteraction.h
/usr/include/glib-2.0/gio/gtlspassword.h
/usr/include/glib-2.0/gio/gtlsserverconnection.h
/usr/include/glib-2.0/gio/gvfs.h
/usr/include/glib-2.0/gio/gvolume.h
/usr/include/glib-2.0/gio/gvolumemonitor.h
/usr/include/glib-2.0/gio/gzlibcompressor.h
/usr/include/glib-2.0/gio/gzlibdecompressor.h
/usr/include/glib-2.0/glib-object.h
/usr/include/glib-2.0/glib-unix.h
/usr/include/glib-2.0/glib.h
/usr/include/glib-2.0/glib/deprecated/gallocator.h
/usr/include/glib-2.0/glib/deprecated/gcache.h
/usr/include/glib-2.0/glib/deprecated/gcompletion.h
/usr/include/glib-2.0/glib/deprecated/gmain.h
/usr/include/glib-2.0/glib/deprecated/grel.h
/usr/include/glib-2.0/glib/deprecated/gthread.h
/usr/include/glib-2.0/glib/galloca.h
/usr/include/glib-2.0/glib/garray.h
/usr/include/glib-2.0/glib/gasyncqueue.h
/usr/include/glib-2.0/glib/gatomic.h
/usr/include/glib-2.0/glib/gbacktrace.h
/usr/include/glib-2.0/glib/gbase64.h
/usr/include/glib-2.0/glib/gbitlock.h
/usr/include/glib-2.0/glib/gbookmarkfile.h
/usr/include/glib-2.0/glib/gbytes.h
/usr/include/glib-2.0/glib/gcharset.h
/usr/include/glib-2.0/glib/gchecksum.h
/usr/include/glib-2.0/glib/gconvert.h
/usr/include/glib-2.0/glib/gdataset.h
/usr/include/glib-2.0/glib/gdate.h
/usr/include/glib-2.0/glib/gdatetime.h
/usr/include/glib-2.0/glib/gdir.h
/usr/include/glib-2.0/glib/genviron.h
/usr/include/glib-2.0/glib/gerror.h
/usr/include/glib-2.0/glib/gfileutils.h
/usr/include/glib-2.0/glib/ggettext.h
/usr/include/glib-2.0/glib/ghash.h
/usr/include/glib-2.0/glib/ghmac.h
/usr/include/glib-2.0/glib/ghook.h
/usr/include/glib-2.0/glib/ghostutils.h
/usr/include/glib-2.0/glib/gi18n-lib.h
/usr/include/glib-2.0/glib/gi18n.h
/usr/include/glib-2.0/glib/giochannel.h
/usr/include/glib-2.0/glib/gkeyfile.h
/usr/include/glib-2.0/glib/glib-autocleanups.h
/usr/include/glib-2.0/glib/glib-typeof.h
/usr/include/glib-2.0/glib/glist.h
/usr/include/glib-2.0/glib/gmacros.h
/usr/include/glib-2.0/glib/gmain.h
/usr/include/glib-2.0/glib/gmappedfile.h
/usr/include/glib-2.0/glib/gmarkup.h
/usr/include/glib-2.0/glib/gmem.h
/usr/include/glib-2.0/glib/gmessages.h
/usr/include/glib-2.0/glib/gnode.h
/usr/include/glib-2.0/glib/goption.h
/usr/include/glib-2.0/glib/gpattern.h
/usr/include/glib-2.0/glib/gpoll.h
/usr/include/glib-2.0/glib/gprimes.h
/usr/include/glib-2.0/glib/gprintf.h
/usr/include/glib-2.0/glib/gqsort.h
/usr/include/glib-2.0/glib/gquark.h
/usr/include/glib-2.0/glib/gqueue.h
/usr/include/glib-2.0/glib/grand.h
/usr/include/glib-2.0/glib/grcbox.h
/usr/include/glib-2.0/glib/grefcount.h
/usr/include/glib-2.0/glib/grefstring.h
/usr/include/glib-2.0/glib/gregex.h
/usr/include/glib-2.0/glib/gscanner.h
/usr/include/glib-2.0/glib/gsequence.h
/usr/include/glib-2.0/glib/gshell.h
/usr/include/glib-2.0/glib/gslice.h
/usr/include/glib-2.0/glib/gslist.h
/usr/include/glib-2.0/glib/gspawn.h
/usr/include/glib-2.0/glib/gstdio.h
/usr/include/glib-2.0/glib/gstrfuncs.h
/usr/include/glib-2.0/glib/gstring.h
/usr/include/glib-2.0/glib/gstringchunk.h
/usr/include/glib-2.0/glib/gstrvbuilder.h
/usr/include/glib-2.0/glib/gtestutils.h
/usr/include/glib-2.0/glib/gthread.h
/usr/include/glib-2.0/glib/gthreadpool.h
/usr/include/glib-2.0/glib/gtimer.h
/usr/include/glib-2.0/glib/gtimezone.h
/usr/include/glib-2.0/glib/gtrashstack.h
/usr/include/glib-2.0/glib/gtree.h
/usr/include/glib-2.0/glib/gtypes.h
/usr/include/glib-2.0/glib/gunicode.h
/usr/include/glib-2.0/glib/guri.h
/usr/include/glib-2.0/glib/gutils.h
/usr/include/glib-2.0/glib/guuid.h
/usr/include/glib-2.0/glib/gvariant.h
/usr/include/glib-2.0/glib/gvarianttype.h
/usr/include/glib-2.0/glib/gversion.h
/usr/include/glib-2.0/glib/gversionmacros.h
/usr/include/glib-2.0/glib/gwin32.h
/usr/include/glib-2.0/glibconfig.h
/usr/include/glib-2.0/gmodule.h
/usr/include/glib-2.0/gobject/gbinding.h
/usr/include/glib-2.0/gobject/gboxed.h
/usr/include/glib-2.0/gobject/gclosure.h
/usr/include/glib-2.0/gobject/genums.h
/usr/include/glib-2.0/gobject/glib-enumtypes.h
/usr/include/glib-2.0/gobject/glib-types.h
/usr/include/glib-2.0/gobject/gmarshal.h
/usr/include/glib-2.0/gobject/gobject-autocleanups.h
/usr/include/glib-2.0/gobject/gobject.h
/usr/include/glib-2.0/gobject/gobjectnotifyqueue.c
/usr/include/glib-2.0/gobject/gparam.h
/usr/include/glib-2.0/gobject/gparamspecs.h
/usr/include/glib-2.0/gobject/gsignal.h
/usr/include/glib-2.0/gobject/gsourceclosure.h
/usr/include/glib-2.0/gobject/gtype.h
/usr/include/glib-2.0/gobject/gtypemodule.h
/usr/include/glib-2.0/gobject/gtypeplugin.h
/usr/include/glib-2.0/gobject/gvalue.h
/usr/include/glib-2.0/gobject/gvaluearray.h
/usr/include/glib-2.0/gobject/gvaluecollector.h
/usr/include/glib-2.0/gobject/gvaluetypes.h
/usr/lib32/glib-2.0/include/glibconfig.h
/usr/lib64/glib-2.0/include/glibconfig.h
/usr/lib64/libgio-2.0.so
/usr/lib64/libglib-2.0.so
/usr/lib64/libgmodule-2.0.so
/usr/lib64/libgobject-2.0.so
/usr/lib64/libgthread-2.0.so
/usr/lib64/pkgconfig/gio-2.0.pc
/usr/lib64/pkgconfig/gio-unix-2.0.pc
/usr/lib64/pkgconfig/glib-2.0.pc
/usr/lib64/pkgconfig/gmodule-2.0.pc
/usr/lib64/pkgconfig/gmodule-export-2.0.pc
/usr/lib64/pkgconfig/gmodule-no-export-2.0.pc
/usr/lib64/pkgconfig/gobject-2.0.pc
/usr/lib64/pkgconfig/gthread-2.0.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgio-2.0.so
/usr/lib32/libglib-2.0.so
/usr/lib32/libgmodule-2.0.so
/usr/lib32/libgobject-2.0.so
/usr/lib32/libgthread-2.0.so
/usr/lib32/pkgconfig/32gio-2.0.pc
/usr/lib32/pkgconfig/32gio-unix-2.0.pc
/usr/lib32/pkgconfig/32glib-2.0.pc
/usr/lib32/pkgconfig/32gmodule-2.0.pc
/usr/lib32/pkgconfig/32gmodule-export-2.0.pc
/usr/lib32/pkgconfig/32gmodule-no-export-2.0.pc
/usr/lib32/pkgconfig/32gobject-2.0.pc
/usr/lib32/pkgconfig/32gthread-2.0.pc
/usr/lib32/pkgconfig/gio-2.0.pc
/usr/lib32/pkgconfig/gio-unix-2.0.pc
/usr/lib32/pkgconfig/glib-2.0.pc
/usr/lib32/pkgconfig/gmodule-2.0.pc
/usr/lib32/pkgconfig/gmodule-export-2.0.pc
/usr/lib32/pkgconfig/gmodule-no-export-2.0.pc
/usr/lib32/pkgconfig/gobject-2.0.pc
/usr/lib32/pkgconfig/gthread-2.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgio-2.0.so.0
/usr/lib64/libgio-2.0.so.0.7100.0
/usr/lib64/libglib-2.0.so.0
/usr/lib64/libglib-2.0.so.0.7100.0
/usr/lib64/libgmodule-2.0.so.0
/usr/lib64/libgmodule-2.0.so.0.7100.0
/usr/lib64/libgobject-2.0.so.0
/usr/lib64/libgobject-2.0.so.0.7100.0
/usr/lib64/libgthread-2.0.so.0
/usr/lib64/libgthread-2.0.so.0.7100.0
/usr/share/gdb/auto-load/usr/lib64/libglib-2.0.so.0.7100.0-gdb.py
/usr/share/gdb/auto-load/usr/lib64/libgobject-2.0.so.0.7100.0-gdb.py

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgio-2.0.so.0
/usr/lib32/libgio-2.0.so.0.7100.0
/usr/lib32/libglib-2.0.so.0
/usr/lib32/libglib-2.0.so.0.7100.0
/usr/lib32/libgmodule-2.0.so.0
/usr/lib32/libgmodule-2.0.so.0.7100.0
/usr/lib32/libgobject-2.0.so.0
/usr/lib32/libgobject-2.0.so.0.7100.0
/usr/lib32/libgthread-2.0.so.0
/usr/lib32/libgthread-2.0.so.0.7100.0
/usr/share/gdb/auto-load/usr/lib32/libglib-2.0.so.0.7100.0-gdb.py
/usr/share/gdb/auto-load/usr/lib32/libgobject-2.0.so.0.7100.0-gdb.py

%files libexec
%defattr(-,root,root,-)
/usr/libexec/glib-compile-schemas

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gapplication.1
/usr/share/man/man1/gdbus-codegen.1
/usr/share/man/man1/gdbus.1
/usr/share/man/man1/gio-querymodules.1
/usr/share/man/man1/gio.1
/usr/share/man/man1/glib-compile-resources.1
/usr/share/man/man1/glib-compile-schemas.1
/usr/share/man/man1/glib-genmarshal.1
/usr/share/man/man1/glib-gettextize.1
/usr/share/man/man1/glib-mkenums.1
/usr/share/man/man1/gobject-query.1
/usr/share/man/man1/gresource.1
/usr/share/man/man1/gsettings.1
/usr/share/man/man1/gtester-report.1
/usr/share/man/man1/gtester.1

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/graphical.target.wants/glib-schemas-firstboot.service
/usr/lib/systemd/system/glib-schemas-firstboot.service
/usr/lib/systemd/system/glib-schemas-trigger.service
/usr/lib/systemd/system/update-triggers.target.wants/glib-schemas-trigger.service

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libgio-2.0.a
/usr/lib64/libglib-2.0.a
/usr/lib64/libgmodule-2.0.a
/usr/lib64/libgobject-2.0.a
/usr/lib64/libgthread-2.0.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/libgio-2.0.a
/usr/lib32/libglib-2.0.a
/usr/lib32/libgmodule-2.0.a
/usr/lib32/libgobject-2.0.a
/usr/lib32/libgthread-2.0.a

%files locales -f glib20.lang
%defattr(-,root,root,-)
