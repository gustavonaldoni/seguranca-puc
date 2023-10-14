from framework.framework_latex import FrameworkLaTeX
from framework.section import SectionItem, Section


def main():
    sections = [
        Section(
            "Mapas de ciberataques",
            [
                SectionItem(
                    "https://cybermap.kaspersky.com/", "Kaspersky CyberThreat Real Time"
                ),
                SectionItem(
                    "https://www.digitalattackmap.com/#anim=1&color=0&country=ALL&list=0&time=18763&view=map", "Digital Attack Map"
                ),
                SectionItem(
                    "https://threatmap.fortiguard.com/", "Fortinet Threat Map"
                ),
                SectionItem(
                    "https://threatmap.checkpoint.com/", "FireEye Threat Map"
                ),
                SectionItem(
                    "https://threatmap.checkpoint.com/", "FireEye CheckPoint Threat Map"
                ),
                SectionItem(
                    "https://www.akamai.com/internet-station/cyber-attacks", "Akamai Attack Map"
                ),
                SectionItem(
                    "https://dciber.org/mapas-de-ameacas/", "DCiber Painel e Mapas de Ameaças"
                )
            ]
        ),

        Section(
            "Sistemas Operacionais para Perícia Forense Computacional e Perícia Computacional",
            [
                SectionItem(
                    "https://www.caine-live.net/", "CAINE"
                ),
                SectionItem(
                    "https://www.gentoo.org/", "Gentoo"
                ),
                SectionItem(
                    "https://www.kali.org/", "Kali"
                ),
                SectionItem(
                    "https://www.parrotsec.org/", "Parrot"
                ),
                SectionItem(
                    "https://tsurugi-linux.org/", "Tsurugi"
                ),
                SectionItem(
                    "https://distrosea.com/", "DistroSea - Distribuições Linux Online"
                ),
                SectionItem(
                    "https://www.onworks.net/", "OnWorks - Distribuições Linux Online"
                )
            ]
        ),

        Section(
            "Ferramentas para Monitoramento e Perícia em Redes de Comunicação",
            [
                SectionItem(
                    "https://www.wireshark.org/download.html", "WireShark - Monitoramento de Redes de Comunicação"
                ),
                SectionItem(
                    "https://www.tcpdump.org/", "TCPDump - Monitoramento de Redes de Comunicação"
                ),
                SectionItem(
                    "https://tools.kali.org/wireless-attacks/wifite", "WiFiTe - Ataques a Redes de Comunicação"
                ),
                SectionItem(
                    "https://wigle.net/", "Wigle - Serviço para Localização de Pontos de Acesso a Redes"
                )
            ]
        ),

        Section(
            "Ferramentas para Perícia em Fontes Abertas (OSINT)",
            [
                SectionItem(
                    "https://www.advisor-bm.com/osint-tools", "Framework OSINT 01"
                ),
                SectionItem(
                    "https://osintframework.com/", "Framework OSINT 02"
                ),
                SectionItem(
                    "https://start.me/p/9Epj7a/osint", "Framework OSINT 03"
                ),
                SectionItem(
                    "https://www.maltego.com/downloads/", "Maltego"
                ),
                SectionItem(
                    "https://github.com/smicallef/spiderfoot", "SpiderFoot"
                ),
                SectionItem(
                    "https://www.shodan.io/", "Shodan Search Engine"
                ),
                SectionItem(
                    "https://gsuite.tools/pt", "Google Suite (GSuite)"
                ),
                SectionItem(
                    "http://web.archive.org/web/sitemap", "WayBack Machine"
                ),
                SectionItem(
                    "https://carbondate.cs.odu.edu/", "Carbon Date"
                ),
                SectionItem(
                    "https://tineye.com/", "TinEye"
                ),
                SectionItem(
                    "https://www.domaintools.com/", "Domain Tools"
                ),
                SectionItem(
                    "https://mxtoolbox.com/SuperTool.aspx", "MxToolBox"
                ),
                SectionItem(
                    "https://mha.azurewebsites.net/", "MHA - Análise de Cabeçalho de E-mail"
                ),
                SectionItem(
                    "https://sistemas.procon.sp.gov.br/evitesite/list/evitesites.php", "Black List for Websites"
                ),
                SectionItem(
                    "https://haveibeenpwned.com/", "Vazamento de Dados"
                ),
                SectionItem(
                    "https://pastebin.com/", "Vazamento de Senhas e E-Mails"
                ),
                SectionItem(
                    "http://servicos.receita.fazenda.gov.br/Servicos/cnpjreva/Cnpjreva_Solicitacao.asp", "Consulta CNPJ"
                ),
                SectionItem(
                    "https://www.keplaca.com/", "KePlaca"
                ),
            ]
        ),

        Section(
            "Ferramentas para Perícia em Dispositivos de Uso Pessoal (Smartphones)",
            [
                SectionItem(
                    "https://www.mobiledit.com/mobiledit-forensic", "MobilEdit Forensic Tools - Extração e Análise"
                ),
                SectionItem(
                    "https://www.oxygen-forensic.com/en/products/oxygen-forensic-detective", "Oxygen Forensic Tools - Extração e Análise"
                ),
                SectionItem(
                    "https://belkasoft.com/es/bat", "Belkasoft Evidence Center - Extração e Análise"
                ),
                SectionItem(
                    "https://forensicdesk.com/docs/english/overview", "Forensic Desk Extraction Tools - Extração e Análise de Mensagens"
                ),
                SectionItem(
                    "https://www.cellebrite.com/pt/ufed-ultimate-4/", "UFED Cellebrite - Extração e Indexação"
                ),
                SectionItem(
                    "https://www.cgsecurity.org/wiki/TestDisk_Download", "PhotoRec - Recuperação de Dados Excluídos e Data Carving"
                ),
                SectionItem(
                    "https://developer.android.com/studio/releases/platform-tools", "ADB SDK and Tools - Modo ADB para Dispositivos Android"
                ),
                SectionItem(
                    "https://developer.android.com/studio/command-line/adb?hl=pt-br", "Android Debug Bridge - Developer Mode"
                ),
                SectionItem(
                    "https://developer.android.com/studio/command-line/adb?hl=pt-br", "Modo ADB for Developers"
                ),
                SectionItem(
                    "https://support.apple.com/pt-br/HT210384", "iTunes - Modo Bridge para Apple iOS"
                ),
                SectionItem(
                    "https://fbidb.io/docs/overview/", "iOS Development Bridge (idb)"
                )
            ]
        ),

        Section(
            "Ferramentas para Perícia em Dispositivos de Uso Pessoal (Notebooks e Desktops)",
            [
                SectionItem(
                    "https://www.belarc.com/products/belarc-advisor", "Belarc Advisor"
                ),
                SectionItem(
                    "https://accessdata.com/product-download/ftk-imager-version-4-5", "FTK Imager - Extração de Evidências e Geração de Imagens Forenses"
                ),
                SectionItem(
                    "https://sourceforge.net/projects/air-imager/files/air-imager/air-2.0.0/", "AIR - Gerador de Imagem Forense"
                ),
                SectionItem(
                    "https://github.com/keydet89/RegRipper3.0", "RegRipper - Análise de Registros do Sistema Operacional"
                ),
                SectionItem(
                    "https://www.volatilityfoundation.org/releases", "Volatility - Análise de DUMP de Memória Principal"
                ),
                SectionItem(
                    "https://www.osforensics.com/tools/volatility-workbench.html", "Volatility WorkBench - Análise de DUMP de Memória Principal"
                ),
                SectionItem(
                    "https://github.com/sepinf-inc/IPED", "IPED - Autopsy - Indexação, Processamento e Análise Forense de Evidências"
                ),
                SectionItem(
                    "https://www.autopsy.com/download/", "Autopsy - Indexação, Processamento e Análise Forense de Evidências"
                )
            ]
        ),

        Section(
            "Ferramentas para Perícia em Imagens",
            [
                SectionItem(
                    "https://thispersondoesnotexist.com/", "Fake Person Generator"
                ),
                SectionItem(
                    "https://tineye.com/", "TinEye - Engenharia Reversa para Buscas Baseadas em Imagem"
                ),
                SectionItem(
                    "https://29a.ch/photo-forensics/#forensic-magnifier", "Forensically - Análise Preliminar de Imagens e Extração de Metadados"
                ),
                SectionItem(
                    "https://imagej.nih.gov/", "ImageJ - Ferramenta para Manipulação de Imagens Matriciais"
                ),
                SectionItem(
                    "https://imagej.nih.gov/ij/plugins/index.html#filters", "ImageJ - Plugins"
                ),
                SectionItem(
                    "https://www.youtube.com/watch?v=P1OjcHWeuew", "ImageJ - Demonstração de Alguns Filtros"
                ),
                SectionItem(
                    "https://imagej.nih.gov/ij/docs/examples/index.html", "ImageJ - Tutoriais e Documentação"
                ),
                SectionItem(
                    "https://www.gimp.org/", "GIMP - Ferramenta para Manipulação de Imagens"
                ),
                SectionItem(
                    "https://github.com/GuidoBartoli/sherloq", "Sherloq - Processamento e Análise de Imagens"
                ),
                SectionItem(
                    "http://www.pcfreetime.com/formatfactory/", "FormatFactory - Conversor entre Formatos de Mídia"
                ),
                SectionItem(
                    "https://stylesuxx.github.io/steganography/", "Esteganografia em Imagens"
                ),
                SectionItem(
                    "https://mediaarea.net/pt/MediaInfo", "MediaInfo - Extração de Informações Estruturais de Arquivos de Mídia"
                ),
            ]
        ),

        Section(
            "Ferramentas para Perícia Forense Computacional Em Áudios e Vídeos",
            [
                SectionItem(
                    "https://www.nchsoftware.com/videopad/index.html", "VideoPad - Ferramenta para Edição e Análise de Vídeo Digital"
                ),
                SectionItem(
                    "https://www.virtualdub.org/", "VirtualDub - Ferramenta para Manipulação de Vídeo"
                ),
                SectionItem(
                    "https://sourceforge.net/projects/x264vfw/", "VirtualDub - CoDec Complementar"
                ),
                SectionItem(
                    "https://www.virtualdub.org/virtualdub_filters.html", "VirtualDub - Filtros"
                ),
                SectionItem(
                    "https://videoprocessing.ai/video_filters/motion-estimation.html", "VirtualDub - Filtro MSU para Compensação de Movimento"
                ),
                SectionItem(
                    "https://www.youtube.com/watch?v=P1OjcHWeuew", "ImageJ - Demonstração de Alguns Filtros"
                ),
                SectionItem(
                    "http://www.watchframebyframe.com/", "WatchFrameByFrame"
                ),
                SectionItem(
                    "https://berify.com/", "Berify"
                ),
                SectionItem(
                    "http://anilyzer.com/", "Anilyzer"
                ),
                SectionItem(
                    "https://mattw.io/youtube-metadata/", "MattW Youtube Metadata"
                ),
                SectionItem(
                    "https://mattw.io/youtube-geofind/location", "MattW Youtube Location"
                ),
                SectionItem(
                    "https://deepware.ai/", "DeepWare - Detecção de Deep Fake"
                ),
            ]
        ),

        Section(
            "Ferramentas para Aúdio",
            [
                SectionItem(
                    "https://www.audacityteam.org/download/", "Audacity - Ferramenta para Edição, Síntese e Análise de Áudio Digital"
                ),
                SectionItem(
                    "https://www.fon.hum.uva.nl/praat/", "Praat - Ferramenta para Síntese e Análise de Áudio Digital"
                ),
                SectionItem(
                    "https://www.nch.com.au/wavepad/index.html", "WavePad - Ferramenta para Edição, Síntese e Análise de Áudio Digital"
                ),
                SectionItem(
                    "https://www.audiotext.com.br/", "AudioText - Transcrição Profissional de Áudio"
                ),
                SectionItem(
                    "https://www.nch.com.au/scribe/index.html", "Express Scribe - Ferramenta para Transcrição de Áudio"
                )
                
            ]
        ),

        Section(
            "Utilitários - Análise Hexadecimal de Arquivos/Bytes, Formatos de Arquivos e Geração de HASH",
            [
                SectionItem(
                    "https://mh-nexus.de/en/hxd/", "Ferramenta HxD"
                ),
                SectionItem(
                    "https://hexeditor.en.softonic.com/", "Ferramenta HexEditor"
                ),
                SectionItem(
                    "https://www.fileformat.info/index.htm", "FileFormat.Info"
                ),
                SectionItem(
                    "https://www.slavasoft.com/hashcalc/", "Ferramenta HashCalc"
                ),
                SectionItem(
                    "https://md5file.com/calculator", "MD5 Hash Online"
                ),
                SectionItem(
                    "https://www.nirsoft.net/utils/hash_my_files.html", "HashMyFiles"
                ),
                SectionItem(
                    "https://winmerge.org/downloads/?lang=pt_br", "WinMerge"
                )
            ]
        ),

        Section(
            "Bibliografia",
            [
                SectionItem(
                    "https://www.amazon.com.br/Investiga%C3%A7%C3%A3o-Digital-em-Fontes-Abertas/dp/8574528145", "Investigação Digital em Fontes Abertas"
                ),
                SectionItem(
                    "https://www.amazon.com.br/Per%C3%ADcia-Forense-Digital-Pr%C3%A1tico-Operacional/dp/8575227920", "Perícia Forense Digital: Guia Prático com Uso do Sistema Operacional Windows"
                ),
                SectionItem(
                    "https://www.amazon.com.br/Deep-Web-Investiga%C3%A7%C3%A3o-Submundo-Internet/dp/8574529370/ref=pd_lpo_3?pd_rd_i=8574529370&psc=1", "Deep Web: Investigação no Submundo da Internet"
                ),
                SectionItem(
                    "https://www.amazon.com.br/Tratado-Computa%C3%A7%C3%A3o-Forense-Jesus-Antonio/dp/8576253356/ref=asc_df_8576253356/?hvadid=379787347388&hvpos=&hvnetw=g&hvrand=3143330243853780134&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9101232&hvtargid=pla-397665041735&psc=1", "Tratado de Computação Forense"
                ),
                SectionItem(
                    "https://www.amazon.com.br/Per%C3%ADcia-Digital-Investiga%C3%A7%C3%A3o-An%C3%A1lise-Forense/dp/8576253704/ref=asc_df_8576253704/?hvadid=379765738259&hvpos=&hvnetw=g&hvrand=3143330243853780134&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9101232&hvtargid=pla-809950589249&psc=1", "Perícia Digital: Da Investigação à Análise Forense"
                )
            ]
        )
    ]

    f = FrameworkLaTeX("framework")
    f.sections = sections

    f.generate_tex()


if __name__ == "__main__":
    main()
