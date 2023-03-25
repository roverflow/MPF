import Head from "next/head";
import Image from "next/image";
import Link from "next/link";
import { Inter } from "next/font/google";
import styles from "@/styles/Home.module.css";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <>
      <Head>
        <title>MPF</title>
        <meta name="description" content="Missing Person Finder" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/aams.svg" />
      </Head>
      <main className={styles.main}>
        <div className={styles.description}>
          <p>
            Get started by uploading&nbsp;
            <code className={styles.code}>Your Missing Person</code>
          </p>
          <div>
            <Link href="/about">
              By <code className={styles.code}>Team Threshold</code>
            </Link>
          </div>
        </div>

        <Link href={`/`} className={styles.center}>
          <Image
            src={require("/assets/mpf.png")}
            alt="mpfLogo"
            style={{ width: "100%", height: "100%" }}
            priority
          />
        </Link>

        <div className={styles.grid}>
          <a
            href="https://nextjs.org/docs?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>Upload</h2>
            <p className={inter.className}>Upload your missing person.</p>
          </a>

          <a
            href="https://nextjs.org/learn?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              List
              {/* <span>-&gt;</span> */}
            </h2>
            <p className={inter.className}>List all your missing people.</p>
          </a>

          <a
            href="https://vercel.com/templates?framework=next.js&utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Found
              {/* <span>-&gt;</span> */}
            </h2>
            <p className={inter.className}>View found people.</p>
          </a>

          <a
            href="https://vercel.com/new?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
            className={styles.card}
            target="_blank"
            rel="noopener noreferrer"
          >
            <h2 className={inter.className}>
              Profile
              {/* <span>-&gt;</span> */}
            </h2>
            <p className={inter.className}>View your profile.</p>
          </a>
        </div>
      </main>
    </>
  );
}
