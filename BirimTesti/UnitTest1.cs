using BusinessLayer.Concrete;
using DataAccessLayer.Abstract;
using DataAccessLayer.EntityFramework;
using EntityLayer.Concrete;
using Moq;

namespace BirimTest
{
    public class Tests
    {
        [SetUp]
        public void Setup()
        {
        }

        [Test]
        public void Calisanlar_CalisanEkleTest()
        {
            var calisanlarControl = new CalisanlarManager (new EfCalisanlarDal());
            Assert.Pass();
        }

        [Test]
        public void GetList_CalisanlarTest()
        {
            // Arrange
            var mockCalisanlarDal = new Mock<ICalisanlarDal>();
            var calisanlarList = new List<Calisanlar>
        {
            new Calisanlar { calisanId = 7, adSoyad = "Test 1", seraId = 1, telefon= "2134", adres = "Elazýð", maas = 123, iban= "1234" },
            new Calisanlar { calisanId = 8, adSoyad = "Test 2", seraId = 2, telefon= "2134", adres = "Elazýð", maas = 123, iban= "1234" },
       
        };
            mockCalisanlarDal.Setup(x => x.GetList()).Returns(calisanlarList);
            var calisanlarManager = new CalisanlarManager(mockCalisanlarDal.Object);

            // Act
            var result = calisanlarManager.TGetList();

            // Assert
            Assert.AreEqual(calisanlarList, result);
        }

        [Test]
        public void TAdd_CalisanlarTest()
        {
            // Arrange
            var mockCalisanlarDal = new Mock<ICalisanlarDal>();
            var calisanlarManager = new CalisanlarManager(mockCalisanlarDal.Object);
            var calisan = new Calisanlar { calisanId = 9, adSoyad = "Test 3", seraId = 2, telefon = "1234", adres = "Elazýð", maas = 123, iban = "12346" };
            var successFlag = false;

            // Act
            calisanlarManager.TAdd(calisan);
            successFlag = true;
            // Assert
            mockCalisanlarDal.Verify(x => x.Insert(calisan), Times.Once);
            Assert.IsTrue(successFlag);
        }

        [Test]
        public void TAdd_DegerlendirmeTest()
        {
            // Arrange
            var mockDegerlendirmelerDal = new Mock<IDegerlendirmelerDal>();
            var degerlendirmelerManager = new DegerlendirmelerManager(mockDegerlendirmelerDal.Object);

            var degerlendirme = new Degerlendirmeler { degerlendirmeId = 4, gorsel = "deneme.jpg", baslik = "test deneme", aciklama = "deneme aciklama" };
            var successFlag = false;

            // Act
            degerlendirmelerManager.TAdd(degerlendirme);
            successFlag = true;
            // Assert
            mockDegerlendirmelerDal.Verify(x => x.Insert(degerlendirme), Times.Once);
            Assert.IsTrue(successFlag);
        }

     

    }
}