%global tl_name beamerswitch
%global tl_revision 64182

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.9
Release:	%{tl_revision}.1
Summary:	Convenient mode selection in Beamer documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/beamerswitch
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamerswitch.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This class is a wrapper around the beamer class to make it easier to use
the same document to generate the different forms of the presentation:
the slides themselves, an abbreviated slide set for transparencies or
online reference, an n-up handout version (various layouts are
provided), and a transcript or set of notes using the article class. The
class provides a variety of handout layouts, and allows the mode to be
chosen from the command line (without changing the document itself).

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamerswitch
%dir %{_datadir}/texmf-dist/source/latex/beamerswitch
%dir %{_datadir}/texmf-dist/tex/latex/beamerswitch
%doc %{_datadir}/texmf-dist/doc/latex/beamerswitch/README.md
%doc %{_datadir}/texmf-dist/doc/latex/beamerswitch/beamerswitch-example-article.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerswitch/beamerswitch-example-handout.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerswitch/beamerswitch-example-trans.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerswitch/beamerswitch-example.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamerswitch/beamerswitch-example.tex
%doc %{_datadir}/texmf-dist/doc/latex/beamerswitch/beamerswitch.pdf
%doc %{_datadir}/texmf-dist/source/latex/beamerswitch/Makefile
%doc %{_datadir}/texmf-dist/source/latex/beamerswitch/beamerswitch.dtx
%{_datadir}/texmf-dist/tex/latex/beamerswitch/beamerswitch.cls
