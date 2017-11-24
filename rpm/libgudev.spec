Name:           libgudev
Version:        232
Release:        1
Summary:        GObject-based wrapper library for libudev

License:        LGPLv2+
URL:            https://wiki.gnome.org/Projects/libgudev
Source0:        https://download.gnome.org/sources/libgudev/%{version}/%{name}-%{version}.tar.xz

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(udev)
BuildRequires: gettext-devel
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool

%description
This library makes it much simpler to use libudev from programs
already using GObject. It also makes it possible to easily use libudev
from other programming languages, such as Javascript, because of
GObject introspection support.

%package devel
Summary:   Header files for %{name}
Requires:  %{name} = %{version}-%{release}

%description devel
This package is necessary to build programs using %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

# Disable gtk-doc
sed -i 's/^DISTCHECK_CONFIGURE_FLAGS/#DISTCHECK_CONFIGURE_FLAGS/g' Makefile.am
sed -i '/docs\/Makefile/d' configure.ac

%build
autoreconf -vfi
%configure --disable-umockdev
make %{?_smp_mflags}

%install
%makeinstall
rm %{buildroot}%{_libdir}/*.la

%check
make check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING
%{_libdir}/libgudev-1.0.so.*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib

%files devel
%doc NEWS
%{_libdir}/libgudev-1.0.so
%dir %{_includedir}/gudev-1.0
%dir %{_includedir}/gudev-1.0/gudev
%{_includedir}/gudev-1.0/gudev/*.h
%{_datadir}/gir-1.0/GUdev-1.0.gir
%{_libdir}/pkgconfig/gudev-1.0*
