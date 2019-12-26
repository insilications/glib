#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glib
Version  : 2.62.4
Release  : 106
URL      : https://download.gnome.org/sources/glib/2.62/glib-2.62.4.tar.xz
Source0  : https://download.gnome.org/sources/glib/2.62/glib-2.62.4.tar.xz
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
Requires: glib-license = %{version}-%{release}
Requires: glib-locales = %{version}-%{release}
Requires: glib-services = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : dbus-dev
BuildRequires : dbus-dev32
BuildRequires : desktop-file-utils
BuildRequires : elfutils-dev
BuildRequires : elfutils-dev32
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glib-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : libffi-dev
BuildRequires : libffi-dev32
BuildRequires : libxml2-dev
BuildRequires : libxml2-dev32
BuildRequires : pcre-dev
BuildRequires : pcre-dev32
BuildRequires : shared-mime-info
BuildRequires : systemd-dev
BuildRequires : systemd-dev32
BuildRequires : tzdata
BuildRequires : util-linux-dev
BuildRequires : util-linux-dev32
BuildRequires : which
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
Patch1: 0001-gio-Support-a-stateless-configuration-for-compiled-G.patch
Patch2: xdg-path.patch
Patch3: wakeups.patch
Patch4: gerror-return-on-null.patch
Patch5: gmodule-avx.patch
Patch6: 0001-Remove-debugging-in-gspawn.c.patch
Patch7: add-multilib-config.patch
Patch8: 0001-Check-for-32bit-linker-flag-when-creating-resource-f.patch

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
Requires: glib-license = %{version}-%{release}
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
Requires: glib-license = %{version}-%{release}

%description lib
lib components for the glib package.


%package lib32
Summary: lib32 components for the glib package.
Group: Default
Requires: glib-data = %{version}-%{release}
Requires: glib-license = %{version}-%{release}

%description lib32
lib32 components for the glib package.


%package libexec
Summary: libexec components for the glib package.
Group: Default
Requires: glib-config = %{version}-%{release}
Requires: glib-license = %{version}-%{release}

%description libexec
libexec components for the glib package.


%package license
Summary: license components for the glib package.
Group: Default

%description license
license components for the glib package.


%package locales
Summary: locales components for the glib package.
Group: Default

%description locales
locales components for the glib package.


%package services
Summary: services components for the glib package.
Group: Systemd services

%description services
services components for the glib package.


%prep
%setup -q -n glib-2.62.4
cd %{_builddir}/glib-2.62.4
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
pushd ..
cp -a glib-2.62.4 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1577384143
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -fstack-protector-strong -mzero-caller-saved-regs=used "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dinstalled_tests=false  builddir
ninja -v -C builddir
pushd ../build32
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
meson --libdir=lib32 --prefix=/usr --buildtype=plain -Dinstalled_tests=false  builddir
ninja -v -C builddir
popd

%install
mkdir -p %{buildroot}/usr/share/package-licenses/glib
cp %{_builddir}/glib-2.62.4/COPYING %{buildroot}/usr/share/package-licenses/glib/01a6b4bf79aca9b556822601186afab86e8c4fbf
cp %{_builddir}/glib-2.62.4/gmodule/COPYING %{buildroot}/usr/share/package-licenses/glib/01a6b4bf79aca9b556822601186afab86e8c4fbf
pushd ../build32
DESTDIR=%{buildroot} ninja -C builddir install
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
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
/usr/bin/gio-launch-desktop
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
/usr/share/gdb/auto-load/usr/lib32/libglib-2.0.so.0.6200.4-gdb.py
/usr/share/gdb/auto-load/usr/lib32/libgobject-2.0.so.0.6200.4-gdb.py
/usr/share/gdb/auto-load/usr/lib64/libglib-2.0.so.0.6200.4-gdb.py
/usr/share/gdb/auto-load/usr/lib64/libgobject-2.0.so.0.6200.4-gdb.py
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
/usr/include/glib-2.0/glib/gtestutils.h
/usr/include/glib-2.0/glib/gthread.h
/usr/include/glib-2.0/glib/gthreadpool.h
/usr/include/glib-2.0/glib/gtimer.h
/usr/include/glib-2.0/glib/gtimezone.h
/usr/include/glib-2.0/glib/gtrashstack.h
/usr/include/glib-2.0/glib/gtree.h
/usr/include/glib-2.0/glib/gtypes.h
/usr/include/glib-2.0/glib/gunicode.h
/usr/include/glib-2.0/glib/gurifuncs.h
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
/usr/lib64/libgio-2.0.so.0.6200.4
/usr/lib64/libglib-2.0.so.0
/usr/lib64/libglib-2.0.so.0.6200.4
/usr/lib64/libgmodule-2.0.so.0
/usr/lib64/libgmodule-2.0.so.0.6200.4
/usr/lib64/libgobject-2.0.so.0
/usr/lib64/libgobject-2.0.so.0.6200.4
/usr/lib64/libgthread-2.0.so.0
/usr/lib64/libgthread-2.0.so.0.6200.4

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgio-2.0.so.0
/usr/lib32/libgio-2.0.so.0.6200.4
/usr/lib32/libglib-2.0.so.0
/usr/lib32/libglib-2.0.so.0.6200.4
/usr/lib32/libgmodule-2.0.so.0
/usr/lib32/libgmodule-2.0.so.0.6200.4
/usr/lib32/libgobject-2.0.so.0
/usr/lib32/libgobject-2.0.so.0.6200.4
/usr/lib32/libgthread-2.0.so.0
/usr/lib32/libgthread-2.0.so.0.6200.4

%files libexec
%defattr(-,root,root,-)
/usr/libexec/glib-compile-schemas

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glib/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/graphical.target.wants/glib-schemas-firstboot.service
/usr/lib/systemd/system/glib-schemas-firstboot.service
/usr/lib/systemd/system/glib-schemas-trigger.service
/usr/lib/systemd/system/update-triggers.target.wants/glib-schemas-trigger.service

%files locales -f glib20.lang
%defattr(-,root,root,-)

