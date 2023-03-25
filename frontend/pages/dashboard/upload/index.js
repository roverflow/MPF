import { useState, useEffect } from "react";
import Head from "next/head";
import Link from "next/link";
import styles from "@/styles/Home.module.css";
import Layout from "@/layouts/Layout";

const UploadMissing = () => {
  return (
    <>
      <Head>
        <title>MPF</title>
        <meta name="description" content="Missing Person Finder" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/aams.svg" />
      </Head>
      <Layout>
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
          <div className={styles.auth}>
            <form
              className="d-flex flex-column gap-3"
              style={{ width: "500px" }}
            >
              <div className="d-flex flex-column gap-2">
                <label className={styles.code}>Name</label>
                <input
                  onChange={(e) => setEmail(e.target.value)}
                  type="text"
                  name="name"
                  id="name"
                  className={styles.code}
                />
              </div>
              <div className="d-flex flex-column gap-2">
                <label className={styles.code}>Go to Contact</label>
                <input
                  onChange={(e) => setPassword(e.target.value)}
                  type="text"
                  name="contact"
                  id="contact"
                  className={styles.code}
                />
              </div>
              <div className="d-flex flex-column gap-2">
                <label className={styles.code}>Last Location</label>
                <input
                  onChange={(e) => setPassword(e.target.value)}
                  type="text"
                  name="location"
                  id="location"
                  className={styles.code}
                />
              </div>
              <div className="d-flex flex-column gap-2">
                <label className={styles.code}>Fir Number</label>
                <input
                  onChange={(e) => setPassword(e.target.value)}
                  type="text"
                  name="fir"
                  id="fir"
                  className={styles.code}
                />
              </div>
              <div className="d-flex flex-column gap-2">
                <label className={styles.code}>Missing Person Photo</label>
                <input
                  class="form-control form-control-lg"
                  id="formFileLg"
                  type="file"
                />
              </div>
              <div className={styles.btn_base} type="submit">
                <p>Submit</p>
              </div>
            </form>
          </div>
        </main>
      </Layout>
    </>
  );
};

export default UploadMissing;
