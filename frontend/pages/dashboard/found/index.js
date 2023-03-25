import { useState, useEffect } from "react";
import Head from "next/head";
import Link from "next/link";
import styles from "@/styles/Home.module.css";
import Layout from "@/layouts/Layout";
import axios from "axios";

const ShowMissing = () => {
  const [missing, setMissing] = useState(false);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/users/found_person")
      .then((res) => {
        setMissing(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);
  return (
    <>
      <Head>
        <title>MPF</title>
        <meta name="description" content="Missing Person Finder" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <link rel="icon" href="/aams.svg" />
      </Head>
      <Layout>
        <main className={styles.auth_lt}>
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
          <div className={styles.authxy} style={{ marginTop: "1rem" }}>
            {missing &&
              missing.map((item) => {
                return (
                  <div
                    className="card"
                    style={{ width: "18rem", color: "black" }}
                  >
                    <img
                      className="card-img-top"
                      src={item.url}
                      alt="Card image cap"
                    />
                    <div className={`card-body ${styles.code}`}>
                      <h5 className="card-title">{item.name}</h5>
                      <div className="card-text">Contact: {item.contact}</div>
                      <div className="card-text">FIR: {item.fir}</div>
                      <div>
                        {item.found.map((i, index) => {
                          if (index > 2) {
                            return;
                          }
                          return (
                            <div className="card-text">
                              Found at: {i.url} , Accuracy: {i.score}
                              <br />
                            </div>
                          );
                        })}
                      </div>
                    </div>
                  </div>
                );
              })}
          </div>
        </main>
      </Layout>
    </>
  );
};

export default ShowMissing;
